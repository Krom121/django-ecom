from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.post_list, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.product_list, name='shop'),
    path('register/', views.register, name='register'),
]