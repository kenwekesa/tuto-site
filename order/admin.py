from django.contrib import admin

from .models import Order, Client
# Register your models here.


admin.site.register(Order)
admin.site.register(Client)