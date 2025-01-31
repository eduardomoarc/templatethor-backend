from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.template_group.models import TemplateGroup
from apps.template_group.serializers import TemplateGroupSerializer


class TemplateGroupApiView(APIView):

    def get(self, request, pk=None):
        if pk is not None:
            template_group = get_object_or_404(TemplateGroup, pk=pk)
            serializer = TemplateGroupSerializer(template_group)
            return Response(serializer.data)
        template_groups = TemplateGroup.objects.all()
        serializer = TemplateGroupSerializer(template_groups, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TemplateGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        template_group = get_object_or_404(TemplateGroup, pk=pk)
        serializer = TemplateGroupSerializer(template_group, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
