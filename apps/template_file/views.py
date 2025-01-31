from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.template_file.models import TemplateFile
from apps.template_file.serializers import TemplateFileSerializer


class TemplateFileApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk is not None:
            template_file = get_object_or_404(TemplateFile, pk=pk)
            serializer = TemplateFileSerializer(template_file)
            return Response(serializer.data)
        template_files = TemplateFile.objects.all()
        serializer = TemplateFileSerializer(template_files, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TemplateFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        template_file = get_object_or_404(TemplateFile, pk=pk)
        serializer = TemplateFileSerializer(template_file, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
