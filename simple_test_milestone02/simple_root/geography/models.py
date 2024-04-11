from django.db import models
from django.urls import reverse

class Area(models.Model):
    area_name = models.CharField(max_length=200)
    area_type = models.CharField(max_length=200)
    image = models.ImageField(upload_to='area_images/', null=True, blank=True)
 
    def __str__(self):
        return self.area_name

    
class Attraction(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    attraction_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='attraction_images/', blank=True, null=True)
 
    def __str__(self):
        return self.attraction_name
