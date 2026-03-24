from rest_framework import serializers
from .models import ImageFile, VideosFile, Files

class ImageFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageFile
        fields = '__all__'


class VideoFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideosFile
        fields = '__all__'


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = '__all__'