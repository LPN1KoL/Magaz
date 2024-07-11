from .views import *
from django.urls import path

urlpatterns = [
    path('', welcome),
    path('login', login_view),
    path('register', register_view),
    path('logout', logout_view),
    path('get_search', get_search)
]