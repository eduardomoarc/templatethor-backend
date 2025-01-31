from django.apps import AppConfig

from apps import template_group


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.template_group'
