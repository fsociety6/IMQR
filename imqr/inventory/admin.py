from django.contrib import admin

# Register your models here.
from .models import Service, Item, Category

admin.site.register(Service)
admin.site.register(Item)
admin.site.register(Category)
