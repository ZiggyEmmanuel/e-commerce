#payment/views

import stripe
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from order.models import Order, OrderItem
from product.models import Product
from .forms import BillingAddressForm
from .models import BillingAddress
from django.conf import settings

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    
    if not cart:
        return redirect('order:cart_view')
    
    billing_address, created = BillingAddress.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = BillingAddressForm(request.POST, instance=billing_address)
        if form.is_valid():
            billing_address = form.save()

            # Create an order with the billing address
            order = Order.objects.create(user=request.user)

            # Create order items
            line_items = []
            for product_id, quantity in cart.items():
                product = Product.objects.get(id=product_id)
                OrderItem.objects.create(order=order, product=product, quantity=quantity, price=product.current_price())
                
                line_items.append({
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': product.name,
                        },
                        'unit_amount': int(product.current_price() * 100),  # Convert dollars to cents
                    },
                    'quantity': quantity,
                })

            # Create Stripe checkout session
            YOUR_DOMAIN = "http://localhost:8000"  # Update this with your production domain
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=line_items,
                mode='payment',
                success_url=YOUR_DOMAIN + '/payment/success/?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=YOUR_DOMAIN + '/payment/cancel/',
            )

            # Save the Stripe session ID in the order for future reference
            order.stripe_session_id = session.id
            order.save()

            # Clear the cart
            request.session['cart'] = {}

            # Redirect to Stripe checkout
            return redirect(session.url, code=303)

    else:
        form = BillingAddressForm(instance=billing_address)
    
    return render(request, 'payment/checkout.html', {'form': form})

@login_required
@csrf_exempt
def success(request):
    session_id = request.GET.get('session_id')
    order = Order.objects.filter(stripe_session_id=session_id).first()

    if order:
        order.is_paid = True
        order.save()

    return render(request, 'payment/success.html')

@login_required
def cancel(request):
    return render(request, 'payment/cancel.html')
