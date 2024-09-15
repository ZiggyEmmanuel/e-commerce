#order/context_processors.py

from django.conf import settings

def cart_item_count(request):
    cart = request.session.get('cart', {})
    item_count = sum(cart.values())
    return {'cart_item_count': item_count}
