from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    category_id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=1000)
    category_created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.category_name


class Item(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    serial_number = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    details = models.TextField(blank=True, null=True)
    date_of_installation = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    details = models.TextField()
    date_of_service = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def str(self):
        return self.item_id.name + " " + self.item_id.serial_number + "is Updated On :" + self.updated_by


