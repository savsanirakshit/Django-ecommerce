from django.contrib import admin
from .models import BillingAddress, Payment


admin.site.register(BillingAddress)
admin.site.register(Payment)
