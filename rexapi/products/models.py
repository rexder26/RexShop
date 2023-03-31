from django.db import models

class Location(models.Model):
    locationname = models.CharField(max_length=100,unique=True, null=True)

    def __str__(self):
        return self.locationname
    

class product(models.Model):
    productname = models.CharField(max_length=50)
    productdescription = models.CharField(max_length=200)
    productprice = models.FloatField(max_length=50)
    productlocation = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.productname
    

