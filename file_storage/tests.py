from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import *
# Create your tests here.

class ImgModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # creating an object that simulates the "file" to uppload
        test_Imgfile = SimpleUploadedFile(
            name = "test_image.jpg",
            content = b"file_content",      # the 'b' is to let the interpreter know that it would use bytes
            content_type = "image/jpg"
        )
        
        cls.imgobj = ImageFile.objects.create(title="test_objectImg", file=test_Imgfile)
        
    def test_object_name(self):
        self.assertEqual(self.imgobj.title, "test_objectImg")
        
        
    def test_file_uploaded(self):
        self.assertTrue(self.imgobj.file)
        self.assertIn("test_image", self.imgobj.file.name)


class VideoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_video_file = SimpleUploadedFile(
            name = "video_test.mp4",
            content = b"video_content",
            content_type = "video/mp4"
        )
        cls.video_obj = VideosFile.objects.create(title = "test_video_file", file = test_video_file)
        
    def test_object_name(self):
        self.assertEqual(self.video_obj.title, "test_video_file")
        
    def test_file_upload(self):
        self.assertTrue(self.video_obj.file)
        self.assertIn("video_test", self.video_obj.file.name)
        


class FileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_file = SimpleUploadedFile(
            name="test_file.pdf",
            content=b"file_content",
            content_type="file/pdf"
        )
        
        cls.file_obj = Files.objects.create(title = "test_file", file = test_file)
        
    def test_file_name(self):
        self.assertEqual(self.file_obj.title, "test_file")
        
    def test_file_upload(self):
        self.assertTrue(self.file_obj.file)
        self.assertIn("test_file", self.file_obj.file.name)