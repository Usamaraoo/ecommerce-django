from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property  # with this method we can use image by method url more efficiently with relations models otherwise if blank it will give error
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


# This is cart
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):  # this method check if items in the order need shipping or digital
        shipping = False
        order_items = self.orderitem_set.all()
        for i in order_items:
            if i.product.digital is False:
                shipping = True
        return shipping

    @property  # this method calculate total of the all items in cart
    def get_cart_total(self):
        ordered_items = self.orderitem_set.all()
        total = sum(i.get_total_of_single_item() for i in ordered_items)
        return total

    @property  # same as above method but this tim quantity
    def get_cart_items(self):
        ordered_items = self.orderitem_set.all()
        total_quantity = sum([i.quantity for i in ordered_items])
        return total_quantity


# items in  the Cart
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)  # child of Order
    quantity = models.IntegerField(default=0, null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)

    # total for one particular item if it is one or more
    def get_total_of_single_item(self):
        total = self.product.price * self.quantity
        return int(total)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)

    def __str__(self):
        return str(self.address)
