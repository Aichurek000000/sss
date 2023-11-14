from django.db import models
class Video(models.Model):
    file_path = models.FileField(upload_to="video/")
    name = models.CharField(max_length=60)
    likes = models.BigIntegerField(default=0)
    description = models.TextField(null=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name