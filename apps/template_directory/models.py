import uuid
from django.db import models

from apps.template_group.models import TemplateGroup


class TemplateDirectory(models.Model):
    class Meta:
        db_table = 'template_directory'

    def __str__(self):
        return self.name

    uuid = models.CharField(max_length=36, default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=255)
    parent_directory = models.ForeignKey(to='self', on_delete=models.CASCADE, null=True)
    template_group = models.ForeignKey(to=TemplateGroup, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
