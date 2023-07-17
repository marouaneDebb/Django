from django.db import models

# Create your models here.
class Destination(models.Model):
    
    price = models.IntegerField()
    description = models.TextField()
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    offer = models.BooleanField(default=False)
