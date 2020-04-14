from django.db import models
#from django.core.urlresolvers import reverse
from django.urls import reverse


# Create your models here.

class movie(models.Model):
    MovieName=models.CharField(max_length=64)
    Timing=models.DateField()
    Location=models.CharField(max_length=64)

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
