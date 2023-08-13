from django.db import models

# Create your models here.
class Volunteer(models.Model):
    vid = models.IntegerField()
    vname = models.CharField(max_length=40)
    vemail = models.EmailField(max_length=30) 