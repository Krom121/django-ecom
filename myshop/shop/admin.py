from django.contrib import admin
from .models import Category, Product


"""

Below is the registeration of the category model and the
admin model to allow better viewing in the admin page.
prepopulated_fields will allow value to be automatically set 
by using the value of other fields.

"""

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


"""
Below is the product model registration and the admin model.
Here i have used list editable which will allow for muliple rows to be
edited at once.

"""
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}