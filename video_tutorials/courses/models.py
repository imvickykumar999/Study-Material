from django.db import models
import os

class Tutorial(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file_path = models.CharField(max_length=1024)  # Store the relative file path

    @property
    def video_url(self):
        return os.path.join('/media/videos/', self.file_path)

    def __str__(self):
        return self.title
