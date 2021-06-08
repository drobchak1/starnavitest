from rest_framework import serializers
from .models import Post, Like
from blog import services


class PostSerializer(serializers.ModelSerializer):
    likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    is_fan = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "description",
            "likes",
            "author",
            "is_fan",
            "total_likes",
        ]
        extra_kwargs = {
            "likes": {"required": False},
            "author": {"read_only": True},
            "total_likes": {"read_only": True},
            "is_fan": {"read_only": True},
        }
    def get_is_fan(self, obj) -> bool:
        user = self.context.get('request').user
        return services.is_fan(obj, user)

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Like
        fields = '__all__'