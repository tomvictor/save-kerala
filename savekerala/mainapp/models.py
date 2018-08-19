from django.db import models

# Create your models here.


class Camp(models.Model):
    title = models.CharField(max_length=1000)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True,null=True)
    location = models.FloatField(blank=True,null=True)
    contact_no = models.CharField(max_length=20)
    alternative_no = models.CharField(max_length = 20)

    def __str__(self):
        return self.title


