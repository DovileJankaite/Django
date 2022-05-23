from django.db import models

# Create your models here.

class Status(models.Model):
    name = models.CharField('Name', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'status'
        verbose_name_plural = 'statuses'

class Order(models.Model):
    customer_id = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    date = models.DateField('Order Date', null=True, blank=True)
    status_id = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.customer_id} (Date - {self.date}, status - {self.status_id})'

class Customer(models.Model):
    first_name = models.CharField('First name', max_length=100)
    last_name = models.CharField('Last name', max_length=100)
    email = models.CharField('Email', max_length=100)

    def __str__(self):
        return self.email

class Product_order(models.Model):
    order_id = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True)
    product_id = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    quantity = models.CharField('Quantity', max_length=100)

    class Meta:
        verbose_name = 'product order'
        verbose_name_plural = 'product orders'

class Product(models.Model):
    name = models.CharField('Name', max_length=100)
    price = models.CharField('Price', max_length=100)