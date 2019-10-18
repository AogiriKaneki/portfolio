from django.db import models

class Blog(models.Model):
    blog_title = models.CharField(max_length = 350) 
    blog_post = models.TextField() 
    pub_date = models.DateTimeField() 
    blog_image = models.ImageField(upload_to = 'media/images/blog')
