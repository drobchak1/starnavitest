from rest_framework.decorators import action
from rest_framework.response import Response
from blog import services
from users.serializers import UserSerializer


class LikedMixin:
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        """Like post.
        """
        obj = self.get_object()
        services.add_like(obj, request.user)
        return Response()


    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        """Unlike post.
        """
        obj = self.get_object()
        services.remove_like(obj, request.user)
        return Response()
        

    @action(detail=True, methods=['get'])
    def fans(self, request, pk=None):
        """Get all people, who liked post.
        """
        obj = self.get_object()
        fans = services.get_fans(obj)
        serializer = UserSerializer(fans, many=True)
        return Response(serializer.data)