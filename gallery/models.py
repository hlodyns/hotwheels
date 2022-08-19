from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.CharField(max_length=4)
    image = models.ImageField(upload_to = 'images',)
    

    

