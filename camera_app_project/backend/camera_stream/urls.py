from django.urls import path
from . import views

urlpatterns = [
    path('', views.camera_view, name='camera'),
    path('stream/', views.camera_stream, name='camera_stream'),
    path('grayscale/', views.grayscale_view, name='grayscale'),
    path('grayscale/stream/', views.grayscale_stream, name='grayscale_stream'),
]