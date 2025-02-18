import uuid
from django.contrib.auth import get_user_model
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
    image = models.ImageField(upload_to='images/', blank = True, null = True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self): # new
        return reverse('tree_detail', args=[str(self.id)])



class Review(models.Model): # new
    tree = models.ForeignKey(
        Tree,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    review = models.CharField(max_length=255)
    farmer = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.review
    
    def get_absolute_url(self):
        return reverse('tree_review_detail', args=[str(self.id)])