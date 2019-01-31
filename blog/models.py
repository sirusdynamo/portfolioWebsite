from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=250)
    pub_date = models.DateTimeField( blank=True, null=True)
    body_text = models.TextField()
    image = models.ImageField(upload_to='images/',blank=True, null=True)


    def __str__(self):
        return self.blog_title


    def pub_date_pretty(self):
        return self.pub_date.strftime('%B %d %Y')
        

    def summary(self):

        return ''.join(self.body_text.split('.')[0:2])