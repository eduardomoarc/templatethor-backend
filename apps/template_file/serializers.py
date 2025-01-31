from rest_framework import serializers

from apps.template_file.models import TemplateFile


class TemplateFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateFile
        fields = '__all__'
