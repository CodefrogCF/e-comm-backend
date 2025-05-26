from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
#    image = models.ImageField(upload_to='items/')
#    image_url = models.URLField(max_length=255, blank=True, null=True)
    image = models.TextField(null=True, blank=True)
    price = models.CharField(max_length=20)
    stock = models.PositiveIntegerField()
    short_description = models.TextField()
    product_description = models.TextField()

#    def __str__(self):
#        return self.name