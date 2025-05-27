from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    price = models.CharField(max_length=20)
    stock = models.PositiveIntegerField()
    short_description = models.TextField()
    product_description = models.TextField()


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=255)    # optional
    customer_email = models.EmailField()                # optional

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()

def save(self, *args, **kwargs):
    if self.product.stock < self.quantity:
        raise ValueError("Not enough stock for product: " + self.product.name)
    self.product.stock -= self.quantity
    self.product.save()
    super().save(*args, **kwargs)
