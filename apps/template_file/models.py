import uuid
from django.db import models

from apps.template_directory.models import TemplateDirectory


class TemplateFile(models.Model):
    class Meta:
        db_table = 'template_file'

    def __str__(self):
        return self.name

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    uuid = models.CharField(max_length=36, default=uuid.uuid4, unique=True)
    content = models.TextField()
    template_directory = models.ForeignKey(to=TemplateDirectory, on_delete=models.RESTRICT)
