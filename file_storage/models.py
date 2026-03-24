from django.db import models

# Create your models here.
class ImageFile(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='img/')

class VideosFile(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='videos/')

class Files(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/')