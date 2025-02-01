from rest_framework import serializers

from apps.template_directory.models import TemplateDirectory
from apps.template_directory.serializers import TemplateDirectorySerializer
from apps.template_group.models import TemplateGroup


class TemplateGroupSerializer(serializers.ModelSerializer):
    uuid = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    directories = serializers.SerializerMethodField()

    class Meta:
        model = TemplateGroup
        fields = ['uuid', 'name', 'dataset', 'directories', 'created_at', 'updated_at']

    def get_directories(self, obj):
        root_directories = TemplateDirectory.objects.filter(template_group=obj, parent_directory__isnull=True)
        return TemplateDirectorySerializer(root_directories, many=True).data
