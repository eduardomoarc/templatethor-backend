from django.urls import path
from .views import TemplateGroupApiView

urlpatterns = [
    path('template_groups/', TemplateGroupApiView.as_view(), name='template_groups'),
    path('template_groups/<uuid:uuid>/', TemplateGroupApiView.as_view(), name='template_groups_put'),
]