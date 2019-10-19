from django.db import models

class Blog(models.Model):
    blog_title = models.CharField(max_length = 350) 
    blog_post = models.TextField() 
    # blog_summary = models.CharField(max_length=225)
    pub_date = models.DateTimeField() 
    blog_image = models.ImageField(upload_to = 'media/images/blog')
    
    def summary(self):
        return self.blog_post[:100]
    
    def __str__(self):
        return self.blog_title