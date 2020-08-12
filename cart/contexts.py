from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """Ensures cart contents available on every page"""
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0

    for id, quantity in cart.items():
        if quantity is None:
            q = 0
        else:
            q = quantity
            product = get_object_or_404(Product, pk=id)
            total += q * product.price
            product_count += q
            cart_items.append({'id': id, 'quantity': q, 'product': product})

    return {'cart_items': cart_items, 'total': total,
            'product_count': product_count}
