from rest_framework import serializers

from apps.template_group.models import TemplateGroup


class TemplateGroupSerializer(serializers.ModelSerializer):
    uuid = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = TemplateGroup
        fields = ['uuid', 'name', 'dataset', 'created_at', 'updated_at']
