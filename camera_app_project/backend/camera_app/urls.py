from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import internal_get, external_get, ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/internal-get/', internal_get, name='internal-get'),
    path('api/external-get/', external_get, name='external-get'),
    path('camera/', include('camera_stream.urls')),  # 攝影機相關URLs
]