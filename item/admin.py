from django.contrib import admin
#add the model into the admin page
from .models import Category, Item


# Register your models here.
#item (from models.py the class) DB access into to admin page
admin.site.register(Category)
admin.site.register(Item)
