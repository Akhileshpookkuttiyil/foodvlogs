from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def cart_details(request, tot=0, count=0, ct_items=None):
    try:
        ct = cart_list.objects.get(cart_id=c_id(request))
        ct_items = items.objects.filter(cart=ct, active=True)
        for item in ct_items:
            tot += (item.products.price * item.quantity)
            count += item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', {'cart_items': ct_items, 'total_price': tot, 'count': count})


def c_id(request):
    ct_id = request.session.session_key
    print(request.session.session_key)
    if not ct_id:
        ct_id = request.session.create()
        print(request.session.create())
    return ct_id


def add_cart(request, product_id):
    prod = product.objects.get(id=product_id)
    try:
        ct = cart_list.objects.get(cart_id=c_id(request))
    except cart_list.DoesNotExist:
        ct = cart_list.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items = items.objects.get(products=prod, cart=ct)
        if c_items.quantity < c_items.products.stock:
            c_items.quantity += 1
        c_items.save()
    except items.DoesNotExist:
        c_items = items.objects.create(products=prod, quantity=1, cart=ct)
        c_items.save()
    return redirect('cartDetails')


def min_cart(request, product_id):
    ct = cart_list.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(product, id=product_id)
    c_items = items.objects.get(products=prod, cart=ct)
    if c_items.quantity > 1:
        c_items.quantity -= 1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartDetails')


def cart_delete(request, product_id):
    ct = cart_list.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(product, id=product_id)
    c_items = items.objects.get(products=prod, cart=ct)
    c_items.delete()
    return redirect('cartDetails')
