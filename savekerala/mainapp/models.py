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

class Locality(models.Model):
    title = models.CharField(max_length = 50)
    code = models.IntegerField(default=0)
    district = models.ForeignKey(Districts,on_delete=models.CASCADE, default=1)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class Camp(models.Model):
    title = models.CharField(max_length=1000)
    place = models.CharField(max_length=2500, blank=True,null=True)
    # locality = models.CharField(max_length=2500,blank=True,null=True)
    locality = models.ForeignKey(Locality,default=1,on_delete=models.CASCADE)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True,null=True)
    location = models.TextField(blank=True,null=True)
    contact_name = models.CharField(max_length=250,default=None, blank=True,null=True)
    contact_no = models.CharField(max_length=20)
    alt_contact_name = models.CharField(max_length=250, default=None,blank=True,null=True)
    alternative_no = models.CharField(max_length = 20,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    admin = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    # district = models.ForeignKey(Districts, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class ItemType(models.Model):
    title = models.CharField(max_length=100)
    code  = models.IntegerField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title



AVAILABLE = 1
SHORTAGE = 0

STOCK_CHOICES = (
    (AVAILABLE, 'AVILABLE'),
    (SHORTAGE, 'SHORTAGE'),
)


class Item(models.Model):
    title  = models.CharField(max_length = 50)
    item_type = models.ForeignKey(ItemType,on_delete=models.CASCADE)
    camp = models.ForeignKey(Camp,on_delete=models.CASCADE)
    quantity = models.FloatField(default=1)
    unit    = models.CharField(max_length = 50,default="Numbers")
    # excess  = models.BooleanField(default=False)
    stock_status = models.IntegerField(choices=STOCK_CHOICES, default=AVAILABLE)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Hero(models.Model):
    name = models.CharField(max_length=250)
    place = models.CharField(max_length=250, blank=True,null=True)
    rank   = models.IntegerField(unique=True)
    short_dic = models.TextField(blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    mobile_no = models.CharField(max_length=1000, blank=True,null=True)
    email = models.CharField(max_length=1000,blank=True,default=True)
    facebook = models.CharField(max_length=2500, blank=True, null=True)

    def __str__(self):
        return self.name

class Community(models.Model):
    name = models.CharField(max_length=250)
    place = models.CharField(max_length=250)
    rank = models.IntegerField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Feedbacks(models.Model):
    name = models.CharField(max_length=250)
    place = models.CharField(max_length=250)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    content = models.TextField()
    email = models.CharField(max_length=250, blank=True, null=True)
    mobile = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name

class ContactUs(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250, blank=True,null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.name
