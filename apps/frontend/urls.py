from django.urls import path

from apps.frontend.views import index

urlpatterns = [
    path('', index, name='index'),
]