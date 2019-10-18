from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to = 'media/images/')
    summary = models.CharField(max_length = 200)
    link = models.CharField(max_length = 1000)
