from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('kids/',views.Kid,name='Kids'),
    path('women/',views.Woman,name='women'),
    path('men/',views.Man,name='Men'),
    path('unisex/',views.uni,name='Unisex'),
    path('cart/', views.cart, name='cart'),

    path('save-to-cart/', views.save_to_cart, name='save_to_cart'),
    path('remove-from-cart/', views.remove_from_cart, name='remove_from_cart'),
    path('cart_total/',views.cart_total,name='cart_total')
]