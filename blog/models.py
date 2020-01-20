from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title =models.CharField(max_length=30)
    blog_text= models.TextField(max_length=1000)
    blog_img=models.ImageField(upload_to='blog_img/',default=False)

    def __str__(self):
        return self.title