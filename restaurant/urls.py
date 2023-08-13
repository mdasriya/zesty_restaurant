from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu_view, name='menu'),
    path('add_dish/', views.add_dish, name='add_dish'),
    path('create_order/', views.create_order, name='create_order'),
    path('manage_orders/', views.manage_orders, name='manage_orders'),
]
