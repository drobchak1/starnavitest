from rest_framework import generics
from .serializers import RegisterSerializer, UserSerializer, UserActivitySerializer
from rest_framework.permissions import AllowAny
from .models import User

# Create your views here.

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserActivity(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserActivitySerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# Can be done if needed

# class ChangePasswordView(generics.UpdateAPIView):

#     queryset = User.objects.all()
#     permission_classes = (IsAuthenticated,)
#     serializer_class = ChangePasswordSerializer

# class UpdateProfileView(generics.UpdateAPIView):

#     queryset = User.objects.all()
#     permission_classes = (IsAuthenticated,)
#     serializer_class = UpdateUserSerializer