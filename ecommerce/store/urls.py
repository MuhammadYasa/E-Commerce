from django.urls import path
from . import views # maksudnya adalah dia mengimport views ke dalam url

urlpatterns = [
    path('', views.store, name='store'), # '' maksudnya itu home
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout')
]
