from .views import *
from django.urls import path

urlpatterns = [
    path('', welcome),
    path('login', login_view),
    path('register', register_view),
    path('logout', logout_view),
    path('get_search', get_search),
    path('myadmin', admin_test),
    path('myadmin/main', admin_main),
    path('home', home),
    path('myadmin/products', myadmin_products),
    path('myadmin/tags', myadmin_tags),
    path('myadmin/categories', myadmin_categories),
    path('myadmin/orders', myadmin_orders),
    path('myadmin/add_product', admin_add_product)
]