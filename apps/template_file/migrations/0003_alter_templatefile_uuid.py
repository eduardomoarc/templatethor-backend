# Generated by Django 5.1.5 on 2025-01-30 04:18

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('template_file', '0002_alter_templatefile_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templatefile',
            name='uuid',
            field=models.CharField(default=uuid.uuid4, max_length=36, unique=True),
        ),
    ]
