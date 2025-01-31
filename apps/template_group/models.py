import uuid
from django.contrib.auth.models import User
from django.db import models


class TemplateGroup(models.Model):
    class Meta:
        db_table = 'template_group'

    def __str__(self):
        return self.name

    name = models.CharField(max_length=255)
    uuid = models.CharField(max_length=36, default=uuid.uuid4, unique=True)
    dataset = models.TextField(blank=True)
    user_id = models.ForeignKey(to=User, on_delete=models.RESTRICT)
