import uuid
from django.db import models
from django.urls import reverse

# Create your models here.

class Tree(models.Model):
    id = models.UUIDField( # new
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=200)
    farmer = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self): # new
        return reverse('tree_detail', args=[str(self.id)])
