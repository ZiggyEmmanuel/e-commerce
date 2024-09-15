# order/views.py


from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from product.models import Product
from .models import Order, OrderItem
from django.contrib import messages



@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    
    if quantity <= 0:
        return HttpResponse('Quantity must be greater than zero.', status=400)
    
    cart = request.session.get('cart', {})
    
    if product_id in cart:
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity
    
    request.session['cart'] = cart
    return redirect('order:cart_view')

@login_required
def update_cart(request, product_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        
        if quantity <= 0:
            return HttpResponse('Quantity must be greater than zero.', status=400)
        
        cart = request.session.get('cart', {})
        
        if str(product_id) in cart:
            if quantity == 0:
                del cart[str(product_id)]
            else:
                cart[str(product_id)] = quantity
        
        request.session['cart'] = cart
    return redirect('order:cart_view')

@login_required
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('order:cart_view')


@login_required
def cart_view(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    
    cart_items = []
    for product in products:
        quantity = cart[str(product.id)]
        total_price = product.current_price() * quantity
        cart_items.append((product, quantity, total_price))
    
    total_amount = sum(total_price for _, _, total_price in cart_items)
    
    context = {
        'cart_items': cart_items,
        'total_amount': total_amount,
    }
    return render(request, 'order/cart.html', context)


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_items = OrderItem.objects.filter(order=order)
    
    context = {
        'order': order,
        'order_items': order_items,
    }
    return render(request, 'order/order_detail.html', context)

@login_required
def order_success(request):
    return render(request, 'order/order_success.html')

