from django.db import models

class Product(models.Model):
    name = models.CharField("Product Name", max_length=50)
    price = models.IntegerField("Price")
    description = models.CharField("Description", max_length=50)
    category = models.CharField("Category", max_length=50)
    quantity = models.IntegerField("Quantity")
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name