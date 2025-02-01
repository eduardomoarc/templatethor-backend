from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from apps.template_directory.models import TemplateDirectory
from apps.template_group.models import TemplateGroup


class TemplateDirectorySerializer(serializers.ModelSerializer):
    uuid = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    template_group_uuid = serializers.CharField(write_only=False, source="template_group.uuid")
    parent_directory_uuid = serializers.CharField(source="parent_directory.uuid", required=False, allow_null=True)

    class Meta:
        model = TemplateDirectory
        fields = ['uuid', 'name', 'parent_directory_uuid', 'template_group_uuid', 'created_at', 'updated_at']

    def create(self, validated_data):
        validated_data['template_group'] = self._get_template_group_from_data(validated_data)
        validated_data['parent_directory'] = self._get_parent_directory_from_data(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'template_group' in validated_data:
            instance.template_group = self._get_template_group_from_data(validated_data)

        if 'parent_directory' in validated_data:
            instance.parent_directory = self._get_parent_directory_from_data(validated_data)
        return super().update(instance, validated_data)

    @staticmethod
    def _get_template_group_from_data(validated_data):
        template_group_data = validated_data.pop('template_group', {})
        template_group_uuid = template_group_data.get('uuid')
        if not template_group_uuid:
            raise serializers.ValidationError({"template_group_uuid": "This field is required."})
        return get_object_or_404(TemplateGroup, uuid=template_group_uuid)

    @staticmethod
    def _get_parent_directory_from_data(validated_data):
        parent_directory_data = validated_data.pop('parent_directory', {})
        parent_directory_uuid = parent_directory_data.get('uuid')
        if parent_directory_uuid:
            return get_object_or_404(TemplateDirectory, uuid=parent_directory_uuid)
