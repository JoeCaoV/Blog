from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Project(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=155)
    content = RichTextField()

    def __self__(self):
        return self.title

