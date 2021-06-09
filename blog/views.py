from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework import generics,permissions
from blog.mixins import LikedMixin
from rest_framework import viewsets

# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class AuthorPostList(generics.ListCreateAPIView):
    # queryset = Event.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Post.objects.filter(author=self.kwargs['author'])

class PostDetail(LikedMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

class PostViewSet(LikedMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

# likes

# class LikesByDate(generics.ListAPIView):
#     serializer_class = PurchaseSerializer

#     def get_queryset(self):
#         """
#         Optionally restricts the returned purchases to a given user,
#         by filtering against a `username` query parameter in the URL.
#         """
#         queryset = Purchase.objects.all()
#         username = self.request.query_params.get('username')
#         if username is not None:
#             queryset = queryset.filter(purchaser__username=username)
#         return queryset

from collections import Counter
# from datetime import datetime, timedelta
from itertools import groupby

from django_filters import rest_framework as filters
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from blog.filters import DateRangeFilterSet
from .models import Like


class AnaliticView(GenericAPIView):
    queryset = Like.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DateRangeFilterSet

    def get(self, request, format=None):
        queryset = self.get_queryset()
        filtered_queryset = self.filter_queryset(queryset)

        # Queryset needs to be ordered by date for groupby to work correctly
        ordered_queryset = filtered_queryset.order_by('date_of_creation')
        likes_by_date = groupby(ordered_queryset,
                                lambda like: like.date_of_creation.strftime("%Y-%m-%d"))

        analytics = []
        for date_of_creation, likes in likes_by_date:
            count = Counter(like.object_id for like in likes)
            analytics.append(
                {
                    'date': date_of_creation,
                    'total_likes': count['like'],
                    'total_dislikes': count['dislike'],

                }
            )

        return Response(analytics)  