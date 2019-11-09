from django.db import models

class Contact(models.Model):
    email_id = models.CharField(max_length = 50)
    message = models.CharField(max_length = 500)
    att= models.FileField(
        upload_to = 'media/attatchments',
        blank=True,
        )
