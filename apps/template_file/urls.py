from django.urls import path
from .views import TemplateFileApiView

urlpatterns = [
    path('template_files/', TemplateFileApiView.as_view(), name='template_files'),
    path('template_files/<uuid:uuid>/', TemplateFileApiView.as_view(), name='template_files_put'),
]
