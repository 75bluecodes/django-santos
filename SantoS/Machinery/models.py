from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_stock = models.IntegerField()
    product_image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.product_name

