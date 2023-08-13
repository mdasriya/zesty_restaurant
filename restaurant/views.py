import json
from django.shortcuts import render, redirect
from django.conf import settings
import os

def read_dishes_from_json():
    dishes_file_path = os.path.join(settings.BASE_DIR, 'dishes.json')
    with open(dishes_file_path, 'r') as f:
        dishes = json.load(f)
    return dishes

def write_dishes_to_json(dishes):
    dishes_file_path = os.path.join(settings.BASE_DIR, 'dishes.json')
    with open(dishes_file_path, 'w') as f:
        json.dump(dishes, f, indent=4)

def menu_view(request):
    dishes = read_dishes_from_json()
    return render(request, 'restaurant/menu.html', {'dishes': dishes})

def add_dish(request):
    if request.method == 'POST':
        dish_name = request.POST.get('dish_name')
        price = float(request.POST.get('price'))
        availability = request.POST.get('availability') == 'True'
        
        new_dish = {'dish_name': dish_name, 'price': price, 'availability': availability}
        dishes = read_dishes_from_json()
        dishes.append(new_dish)
        write_dishes_to_json(dishes)
        
        return redirect('menu')
    return render(request, 'restaurant/add_dish.html')

def create_order(request):
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        selected_dishes = request.POST.getlist('dishes')
        # Process the order here (e.g., print selected_dishes)
        
        # Update: Get the list of orders and add the new order
        orders = read_orders_from_json()
        new_order = {'customer_name': customer_name, 'dishes': selected_dishes}
        orders.append(new_order)
        write_orders_to_json(orders)
        
        return redirect('menu')
    
    dishes = read_dishes_from_json()
    return render(request, 'restaurant/create_order.html', {'dishes': dishes})

def manage_orders(request):
    orders = read_orders_from_json()
    return render(request, 'restaurant/manage_orders.html', {'orders': orders})

def read_orders_from_json():
    orders_file_path = os.path.join(settings.BASE_DIR, 'orders.json')
    if os.path.exists(orders_file_path):
        with open(orders_file_path, 'r') as f:
            orders = json.load(f)
    else:
        orders = []
    return orders

def write_orders_to_json(orders):
    orders_file_path = os.path.join(settings.BASE_DIR, 'orders.json')
    with open(orders_file_path, 'w') as f:
        json.dump(orders, f, indent=4)
