from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from app2.models import BillingAddress, Payment

from django_countries.fields import CountryField


User = settings.AUTH_USER_MODEL

CATEGORY_CHOICES = {
    ('T', 'touch'),
    ('K', 'keypade'),
    ('B', 'both'),
}


LABEL_CHOICES = {
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger'),
}


class Item(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    desc = models.TextField(max_length=2250)
    img = models.ImageField(upload_to='pics')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("app:details", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("app:add_to_cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("app:remove_from_cart", kwargs={
            'slug': self.slug
        })


class OrderItem(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity *self.item.price

    def get_final_price(self):
        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    start_date = models.DateTimeField(auto_now_add=True,)
    ordered_date = models.DateTimeField()
    billing_address = models.ForeignKey(BillingAddress, null=True, blank=True, on_delete=models.SET_NULL)
    payment = models.ForeignKey(Payment, null=True, blank=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total




