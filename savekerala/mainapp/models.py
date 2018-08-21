from django.db import models
from django.contrib.auth.admin import User
# Create your models here.


class Districts(models.Model):
    title = models.CharField(max_length = 50)
    code = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_camps(self):
        camps = Camp.models.all()
        return camps

class Camp(models.Model):
    title = models.CharField(max_length=1000)
    place = models.CharField(max_length=2500, blank=True,null=True)
    locality = models.CharField(max_length=2500,blank=True,null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True,null=True)
    location = models.TextField(blank=True,null=True)
    contact_no = models.CharField(max_length=20)
    alternative_no = models.CharField(max_length = 20)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    admin = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    district = models.ForeignKey(Districts, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class ItemType(models.Model):
    title = models.CharField(max_length=100)
    code  = models.IntegerField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


class Item(models.Model):
    title  = models.CharField(max_length = 50)
    item_type = models.ForeignKey(ItemType,on_delete=models.CASCADE)
    camp = models.ForeignKey(Camp,on_delete=models.CASCADE)
    quantity = models.FloatField(default=1)
    unit    = models.CharField(max_length = 50,default="Numbers")
    excess  = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

