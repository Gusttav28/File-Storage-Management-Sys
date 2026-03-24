from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import *
from .models import *

# Create your views here.
class ImageFilesViews(viewsets.ModelViewSet):
    queryset = ImageFile.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ImageFileSerializer


class VideoFilesViews(viewsets.ModelViewSet):
    queryset = VideosFile.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = VideoFileSerializer


class FilesViews(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FilesSerializer
    