from django.conf import settings
from django.conf.urls import url
from django.urls import path
from django.conf.urls.static import static
from . import views

app_name = 'shop'

"""

Here there are to differently defined product list patterns one is 
calling product list without any parameters and the other product list by category
which provides a category slug parameter to the view for filtering products.
Product detail passes the id and slug to the view in order to retrieve a product.

"""

urlpatterns = [
    path('product_list/', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, 
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
]