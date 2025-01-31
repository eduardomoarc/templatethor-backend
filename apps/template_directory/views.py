from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.template_directory.models import TemplateDirectory
from apps.template_directory.serializers import TemplateDirectorySerializer


class TemplateDirectoryAPIView(APIView):

    def get(self, request, pk=None):
        if pk is not None:
            template_directory = get_object_or_404(TemplateDirectory, pk=pk)
            serializer = TemplateDirectorySerializer(template_directory)
            return Response(serializer.data)
        template_directories = TemplateDirectory.objects.all()
        serializer = TemplateDirectorySerializer(template_directories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TemplateDirectorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        template_directory = get_object_or_404(TemplateDirectory, pk=pk)
        serializer = TemplateDirectorySerializer(template_directory, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
