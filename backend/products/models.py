from django.db import models


class React(models.Model):
    employee=models.CharField(max_length=30)
    department=models.CharField(max_length=200)


class Product(models.Model):
    ean = models.PositiveBigIntegerField(unique=True)
    category = models.CharField(max_length=64)
    manufacturer = models.CharField(max_length=64) 
    brand = models.CharField(max_length=64)
    product_title = models.CharField(max_length=64)
    image = models.URLField(max_length=1024)

    def __str__(self):
        return self.product_title


class Retailer(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)
    date = models.DateField()
    base_price = models.FloatField()
    shelf_price = models.FloatField()
    promoted_price = models.FloatField()

    def __str__(self):
        return f"{self.product}, {self.retailer} - {self.base_price}"


class ProductRetailer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)
    on_promotion = models.BooleanField(default=False)

    class Meta:
        unique_together = ['product', 'retailer']

    def __str__(self):
        return f"{self.product}, {self.retailer}"


class Promotion(models.Model):
    description = models.CharField(max_length=64)
    product_retailer = models.ForeignKey(ProductRetailer, on_delete=models.CASCADE, related_name='promotion')

    def __str__(self):
        return self.description