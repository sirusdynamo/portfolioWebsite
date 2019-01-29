from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=250)
    pub_date = models.DateTimeField( blank=True, null=True)
    body_text = models.TextField()
    image = models.ImageField(upload_to='images/',blank=True, null=True)