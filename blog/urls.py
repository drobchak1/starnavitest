from rest_framework.routers import DefaultRouter
from .views import PostViewSet
# Создаем router и регистрируем ViewSet
router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = router.urls
app_name = 'blog'