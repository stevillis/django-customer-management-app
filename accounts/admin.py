from django.contrib import admin

from accounts.models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
