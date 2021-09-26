from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
