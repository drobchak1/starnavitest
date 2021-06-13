from rest_framework import serializers
from users.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    User = get_user_model()
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "bio",
            "posts",
            "last_login",
            "last_activity",
        ]
        extra_kwargs = {
            "first_name": {"required": False},
            "last_name": {"required": False},
            "bio": {"required": False},
            "posts": {"required": False},
            "last_login": {"required": False},
            "last_activity": {"required": False},
        }


class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "last_login",
            "last_activity",
        ]


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(write_only=True, allow_null=True, allow_blank=True, required= False)
    last_name = serializers.CharField(write_only=True, allow_null=True, allow_blank=True, required= False)
    bio = serializers.CharField(write_only=True, allow_null=True, allow_blank=True, required= False)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'bio')
        extra_kwargs = {
            "first_name": {"required": False},
            "last_name": {"required": False},
            "bio": {"required": False},
            "posts": {"required": False},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', None),
            last_name=validated_data.get('last_name', None),
            bio=validated_data.get('bio', None),
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user