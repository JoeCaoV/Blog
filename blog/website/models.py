from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Project(models.Model):
    number = models.IntegerField(unique=True)
    title = models.CharField(max_length=155)
    content = RichTextUploadingField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
    date = models.DateTimeField(default=now, editable=False)
    content = models.TextField()

