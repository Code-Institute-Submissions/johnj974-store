from django.shortcuts import get_object_or_404
from products.models import Machinery


def cart_contents(request):
    cart = request.session.get('cart',{})
    cart_items = []
    total = 0
    product_count = 0
    for id, quantity in cart.items():
        product = get_object_or_404(Machinery, pk=id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({'id':id, 'quantity': quantity, 'product': product})
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}