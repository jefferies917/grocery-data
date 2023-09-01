from django.db import models


class React(models.Model):
    employee=models.CharField(max_length=30)
    department=models.CharField(max_length=200)


class Product(models.Model):
    ean = models.PositiveBigIntegerField(unique=True)
    category = models.CharField(max_length=64)
    manufacturer = models.CharField(max_length=64)  # TODO add choice fields to category, manufactuer, brand
    brand = models.CharField(max_length=64)
    product_title = models.CharField(max_length=64)
    image = models.URLField(max_length=1024)


class Retailer(models.Model):
    name = models.CharField(max_length=64)


class Promotion(models.Model):
    description = models.CharField(max_length=64)


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)
    date = models.DateField()
    base_price = models.FloatField()
    shelf_price = models.FloatField()
    promoted_price = models.FloatField()


class ProductRetailer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)
    on_promotion = models.BooleanField(default=False)