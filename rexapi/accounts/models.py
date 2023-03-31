from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    phone = models.IntegerField(null=True)
    email = models.EmailField(max_length=200,null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)
    profile_pic = models.ImageField(default="profile.png",null=True,blank=True)

    def __str__(self) -> str:
        return self.name

    
class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)

    def __str__(self) -> str:
        return self.name
    
class job(models.Model):
    CATEGORY = (
        ('IT','IT'),
        ('Business','Business'),
        ('Marketing','Marketing'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True,choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)
    def __str__(self) -> str:
        return self.name

    
class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    job = models.ForeignKey(job, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200,null=True,choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self) -> str:
        return self.job.name