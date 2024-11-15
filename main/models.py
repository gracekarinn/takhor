from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class ProductakhorModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=15)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    quantity = models.IntegerField()

