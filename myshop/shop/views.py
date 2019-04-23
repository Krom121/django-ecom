from django.shortcuts import render, get_object_or_404
from .models import Category, Product

"""
Below i have the view for the product list where i am quiring the products
by category and filtering them. The if category slug will allow for a parameter to 
optionally filter products.

"""
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

"""

Below is the product detail view which expects a id and slug in order to
retrieve a product. The id is a unique attribute. The slug will provide humanized
and seo friendly urls.

"""
def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'detail.html',
                  {'product': product})