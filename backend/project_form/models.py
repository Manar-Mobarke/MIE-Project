from django.db import models


class ProjectForm(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
