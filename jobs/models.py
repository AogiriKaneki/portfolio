from django.db import models

class Job(models.Model):
    job_title = models.CharField(max_length = 255)
    image = models.ImageField(upload_to = 'images/jobs')
    summary = models.CharField(max_length = 200)