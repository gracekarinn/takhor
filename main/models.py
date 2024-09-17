from django.db import models
import uuid

# Create your models here.
class ProductakhorModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=15)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    quantity = models.IntegerField()