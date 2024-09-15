#payment/admin

from django.contrib import admin
from .models import BillingAddress

@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'country')