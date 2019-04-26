from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('users.urls', namespace='users')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('shop/', include('shop.urls', namespace='shop')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('', include('pages.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
