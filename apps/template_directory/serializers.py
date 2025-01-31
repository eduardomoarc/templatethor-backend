from rest_framework import serializers

from apps.template_directory.models import TemplateDirectory


class TemplateDirectorySerializer(serializers.ModelSerializer):
    uuid = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = TemplateDirectory
        fields = ['uuid', 'name', 'parent_directory', 'template_group', 'created_at', 'updated_at']
