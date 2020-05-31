from django.db import models

# Create your models here.

class Map_List(models.Model):
    location_name = models.CharField(max_length=100)
    map_coordinates_link = models.CharField(max_length=300)

    def __str__(self):
        return self.location_name

class predict_Map_List(models.Model):
    location_name = models.CharField(max_length=100)
    map_coordinates_link = models.CharField(max_length=400)

    def __str__(self):
        return self.location_name
