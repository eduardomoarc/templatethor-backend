import uuid
from django.db import models

from apps.template_group.models import TemplateGroup


class TemplateDirectory(models.Model):
    class Meta:
        db_table = 'template_directory'

    def __str__(self):
        return self.name

    name = models.CharField(max_length=255)
    uuid = models.CharField(max_length=36, default=uuid.uuid4, unique=True)
    parent_id = models.ForeignKey(to='self', on_delete=models.CASCADE, null=True)
    template_group_id = models.ForeignKey(to=TemplateGroup, on_delete=models.RESTRICT)
