from .models import Post, Like
from .serializers import PostSerializer
from rest_framework import generics,permissions
from blog.mixins import LikedMixin
from rest_framework import viewsets
from itertools import groupby
from django_filters import rest_framework as filters
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from blog.filters import DateRangeFilterSet

class AuthorPostList(generics.ListCreateAPIView):
    """List of posts created by user
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Post.objects.filter(author=self.kwargs['author'])


class PostViewSet(LikedMixin, viewsets.ModelViewSet):
    """CRUD operations on posts and likes
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AnaliticsView(GenericAPIView):
    """Get the statistics on number of likes grouped by day. The first date is inclusive, 
    but the second date is exclusive. You should use "?date_from=2021-06-08&date_to=2021-06-10"
    to get likes for 06.08 and 06.09
    """
    queryset = Like.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DateRangeFilterSet

    def get(self, request, format=None):
        queryset = self.get_queryset()
        filtered_queryset = self.filter_queryset(queryset)

        ordered_queryset = filtered_queryset.order_by('date_of_creation')
        likes_by_date = groupby(ordered_queryset,
                                lambda like: like.date_of_creation.strftime("%Y-%m-%d"))

        analytics = []
        for date_of_creation, likes in likes_by_date:
            analytics.append(
                {
                    'date_of_creation': date_of_creation,
                    'total_likes': len(list(likes))
                }
            )

        return Response({'data':analytics})  