from django.db import models

# Create your models here.
class ProductakhorModel(models.Model):
    name = models.CharField(max_length=15)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    quantity = models.IntegerField()