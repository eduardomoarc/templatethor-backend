from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from apps.template_directory.models import TemplateDirectory
from apps.template_file.models import TemplateFile


class TemplateFileSerializer(serializers.ModelSerializer):
    uuid = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    template_directory_uuid = serializers.CharField(source="template_directory.uuid")
    content = serializers.CharField(allow_blank=True)

    class Meta:
        model = TemplateFile
        fields = ['uuid', 'name', 'type', 'content', 'template_directory_uuid', 'created_at', 'updated_at', ]

    def create(self, validated_data):
        validated_data['template_directory'] = self._get_template_directory_from_data(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'template_directory' in validated_data:
            instance.template_directory = self._get_template_directory_from_data(validated_data)
        return super().update(instance, validated_data)

    @staticmethod
    def _get_template_directory_from_data(validated_data):
        template_directory_data = validated_data.pop('template_directory', {})
        template_directory_uuid = template_directory_data.get('uuid')
        if not template_directory_uuid:
            raise serializers.ValidationError({"template_directory_uuid": "This field is required."})
        return get_object_or_404(TemplateDirectory, uuid=template_directory_uuid)

