import uuid
from django.contrib.auth.models import User
from django.db import models


class TemplateGroup(models.Model):
    class Meta:
        db_table = 'template_group'

    def __str__(self):
        return self.name

    uuid = models.CharField(max_length=36, default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=255)
    dataset = models.TextField(blank=True)
    user = models.ForeignKey(to=User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
