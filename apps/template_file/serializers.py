from rest_framework import serializers

from apps.template_file.models import TemplateFile


class TemplateFileSerializer(serializers.ModelSerializer):
    uuid = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = TemplateFile
        fields = ['uuid', 'name', 'type', 'content', 'template_directory', 'created_at', 'updated_at', ]
