from django.urls import path
from .views import TemplateDirectoryAPIView

urlpatterns = [
    path('template_directories/', TemplateDirectoryAPIView.as_view(), name='template_directories'),
    path('template_directories/<uuid:uuid>/', TemplateDirectoryAPIView.as_view(), name='template_directories_put'),
]
