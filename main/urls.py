from django.urls import path
from main.views import *

urlpatterns = [
    path('', home),
    path('shops/<int:id>/', shop),
    path('cart/', cart),
    path('add_to_cart/<int:id>/', add_to_cart),
    path('delete_from_cart/<int:id>/', delete_from_cart),
    path('cart/send_order', send_order)
]