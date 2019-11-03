from django.db import models

class Music(models.Model):
    track_name = models.CharField(max_length = 100)
    track_link = models.URLField(
        blank=True,
    )
    track_thumbnail=models.ImageField(upload_to = 'media/images/Music')
    track_file = models.FileField(
        upload_to = 'media/tracks',
        blank=True,
        )
    def __str__(self):
        return self.track_name
