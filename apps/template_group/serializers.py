from rest_framework import serializers

from apps.template_group.models import TemplateGroup


class TemplateGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateGroup
        fields = '__all__'
