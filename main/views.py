from django.http import HttpResponseNotFound
from django.shortcuts import render
from datetime import date
from main.models import *


def home(request):
    shops = Shop.objects.all()
    products = Product.objects.filter(shop_id=1)
    return render(request, 'shops_page.html', context={'shops': shops, 'products': products})


def shop(request, id: int):
    shops = Shop.objects.all()
    products = Product.objects.filter(shop_id=id)
    return render(request, 'shops_page.html', context={'shops': shops, 'products': products})


def cart(request):
    return render(request, 'shopping_cart_page.html', context={'cart': Cart.objects.all()})


def edit_cart_product(product_id, way, user_id):
    if product_id > len(Product.objects.filter()):
        return HttpResponseNotFound('Wrong number')

    selected_product = Cart.objects.filter(product_id=product_id, user=user_id)

    if len(selected_product) == 0:
        quantity = 0
    else:
        quantity = selected_product[0].quantity
    selected_product.delete()

    cart = Cart()
    cart.product_id = product_id
    if str(way) == '+':
        cart.quantity = quantity + 1
    else:
        cart.quantity = quantity - 1
    cart.user = user_id
    cart.save()

    selected_products = Cart.objects.filter(user=user_id)
    total_price = 0
    for selected_product in selected_products:
        price = Product.objects.filter(id=selected_product.product_id)[0].price
        total_price += float(price) * float(selected_product.quantity)
    return round(total_price, 2)


def add_to_cart(request, id: int):
    total_price = edit_cart_product(id, '+', request.user.id)
    print(request.user.id)
    return render(request, 'shopping_cart_page.html', context={'cart': Cart.objects.all(), 'total_price': total_price})


def delete_from_cart(request, id: int):
    total_price = edit_cart_product(id, '-', request.user.id)
    return render(request, 'shopping_cart_page.html', context={'cart': Cart.objects.all(), 'total_price': total_price})


def send_order(request):
    products = Cart.objects.filter(user=request.user.id)
    for product in products:
        order = Order()
        order.product_id, order.quantity, order.name, order.email, order.phone, order.address, order.total_price = \
            product.product_id, product.quantity, request.POST.get('name'), request.POST.get('email'), \
            request.POST.get('phone'), request.POST.get('address'), request.POST.get('total_price')
        order.date = date.today()
        order.save()
        product.delete()

    finish = 'Congratulations! Your order has been sent. We will connect with you after processing'
    return render(request, 'shopping_cart_page.html', context={'finish': finish})
