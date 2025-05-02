from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to="product_image", blank=True, null=True)

    def __str__(self):
        return f"{self.name}"