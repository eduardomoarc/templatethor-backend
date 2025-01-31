from rest_framework import serializers

from apps.template_directory.models import TemplateDirectory


class TemplateDirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateDirectory
        fields = '__all__'
