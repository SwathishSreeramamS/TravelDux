from django.db import models

# Create your models here.

class packages(models.Model):
    destination = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    duration = models.CharField(max_length=10)
    price = models.IntegerField()
    packager_name = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='uploads/',null=True, blank=True)
    image2 = models.ImageField(upload_to='uploads/',null=True, blank=True)
    image3 = models.ImageField(upload_to='uploads/',null=True, blank=True)
    image4 = models.ImageField(upload_to='uploads/',null=True, blank=True)
    verification = models.CharField(max_length=100,default="Not Verified")

    def __str__(self):
        return self.destination
    
class bookingDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    altPhone = models.IntegerField()
    numTraveller = models.IntegerField()
    destination = models.CharField(max_length=100,default=None)
    packager_name = models.CharField(max_length=100,default=None)

    def __str__(self):
        return self.name