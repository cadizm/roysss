
from __future__ import unicode_literals

from django.db import models

from roysss.apps.common.utils import currency, gen_order_number

from roysss.apps.shop.exceptions import InsufficientInventoryError


class Style(models.Model):
    style_id = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    size = models.CharField(max_length=32)

    def __str__(self):
        return "(%s) %s" % (self.style_id, self.description)


class Item(models.Model):
    style = models.OneToOneField(Style, on_delete=models.PROTECT, primary_key=True)
    amount = models.IntegerField()  # amount in cents (usd)
    description = models.CharField(max_length=256)

    def __str__(self):
        return "(%s) price: %s" % (self.style.style_id, currency(self.amount))


class Inventory(models.Model):
    item = models.OneToOneField(Item, on_delete=models.PROTECT, primary_key=True)
    quantity = models.IntegerField()

    def __str__(self):
        return "(%s) quantity: %d" % (self.item.style.style_id, self.quantity)

    def save(self, **kwargs):
        if self.quantity < 0:
            raise InsufficientInventoryError()

        return super(Inventory, self).save(**kwargs)

    def style_quantity(self):
        return {self.item.style.style_id: self.quantity}


class StripeOrderManager(models.Manager):

    def create(self, **kwargs):
        if 'number' not in kwargs:
            kwargs.update(number=gen_order_number())

        return super(StripeOrderManager, self).create(**kwargs)


class StripeOrder(models.Model):
    objects = StripeOrderManager()

    number = models.CharField(max_length=32)
    uuid = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    name = models.CharField(max_length=128)

    country_code = models.CharField(max_length=8)
    city = models.CharField(max_length=128)
    address_line1 = models.CharField(max_length=128)
    state = models.CharField(max_length=16)
    zipcode = models.CharField(max_length=16)

    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Order #%s" % (self.number)


class OrderItemsManager(models.Manager):

    def total(self):
        total_amount = 0

        for order_item in self.iterator():
            total_amount += order_item.item.amount

        return total_amount


class OrderItems(models.Model):
    objects = OrderItemsManager()

    order = models.ForeignKey(StripeOrder, on_delete=models.PROTECT)
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    quantity = models.IntegerField()

    def __str__(self):
        return "(%s) quantity: %d" % (self.item.style.style_id, self.quantity)


class StripeCharge(models.Model):

    charge_id = models.CharField(max_length=32)
    stripe_order = models.OneToOneField(StripeOrder, on_delete=models.PROTECT, primary_key=True)

    def __str__(self):
        return "Charge #%s" % (self.charge_id)
