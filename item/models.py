from django.db import models

from django.contrib.auth.models import User

# Create your models here.
#TABLE Category 
class Category(models.Model):
    name = models.CharField(max_length=255)

    #(Configurations for the Model)
    class Meta:
        ordering = ('name',)#order by name the objects in category
        verbose_name_plural = 'Categories'  #Because the class is Category in the admin page will add 
                                            #an 's' (Categorys) which is a missspelling so to correct that: 

    # (over ride the string presentation)In the admin page the Categories will be render as "Category Object", to make visible the name of each category:
    def __str__(self):
        return self.name     # self.name => name is the value from "name in the class Category "
    
    #TABLE Item 


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    # (over ride the string presentation)In the admin page for item will be render as "Item Object", to make visible the name of each item:
    def __str__(self):
        return self.name     # self.name => name is the value from "name in the class item "    
