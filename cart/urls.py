from django.urls import path
from . import views

urlpatterns = [
    path('cartDetails', views.cart_details, name='cartDetails'),
    path('add/<int:product_id>/', views.add_cart, name='addCart'),
    path('cartDec/<int:product_id>/', views.min_cart, name='cartDec'),
    path('delete/<int:product_id>/', views.cart_delete, name='delete'),

]
