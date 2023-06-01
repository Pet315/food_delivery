from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=70)
    # is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=70)
    desc = models.TextField(max_length=470, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    # image = models.CharField(max_length=100, null=True)
    # image = models.ImageField(upload_to='products/', null=True)
    # is_visible = models.BooleanField(default=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    user = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.product}'

    class Meta:
        verbose_name_plural = 'Cart'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    name = models.TextField(max_length=70, null=True)
    email = models.TextField(max_length=170)
    phone = models.TextField(max_length=20, null=True)
    address = models.TextField(max_length=270, null=True)
    date = models.DateField(null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product}'
