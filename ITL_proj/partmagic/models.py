from django.db import models

# Create your models here.
class Courses(models.Model):
    class Meta:
        ordering = ['cname']
    cname = models.CharField(max_length=255)
    c_code = models.IntegerField()
    cred = models.IntegerField()

class Pubs(models.Model):
    class Meta:
        ordering = ['auth']
    auth = models.CharField(max_length=1024)
    pub_title = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    pub_date = models.DateField()
