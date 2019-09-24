from django.db import models

# Create your models here.
class Project(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=155)
    content = models.TextField()

    def __self__(self):
        return self.title

class Link(models.Model):
    link = models.CharField(max_length=255)
    projet = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __self__(self):
        return self.link
