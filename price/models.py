from django.db import models

class Fruit(models.Model):
    fruit_name=models.CharField(max_length=100)
    scientific_name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='media')
    country_name=models.CharField(max_length=100)
    price=models.CharField(max_length=100,blank=True)
    def __str__(Self):
        return Self.fruit_name