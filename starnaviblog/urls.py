"""starnaviblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
# from rest_framework.routers import DefaultRouter
from blog.views import PostList, PostDetail, AuthorPostList #PostViewSet
from users.views import UserList, UserDetail, RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# from blog.mixins import LikedMixin

# router = DefaultRouter()
# router.register(r'posts', PostViewSet)

apipatterns = [
    url(r'^', include('blog.urls', 'blog')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view()),
    # path('posts/<int:pk>/like/', LikedMixin.like()),
    path('users/<int:author>/posts/', AuthorPostList.as_view()),
    # Basic auth urls
    path('api-auth/', include('rest_framework.urls')),
    # users urls
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('register/', RegisterView.as_view(), name='auth_register'),
    # Postviewset urls
    url(r'^api/v1/', include((apipatterns, 'blog'), namespace='api')),
    # JWT urls
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
