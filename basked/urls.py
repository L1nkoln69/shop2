from django.urls import path
from . import views


urlpatterns = [
    path('cart_detail', views.cart_detail),
    path('add/<pk>', views.cart_add, name='cart_add'),
    path('remove/<pk>', views.cart_remove)
]