from django.shortcuts import render, redirect, reverse

# Create your views here.


def view_cart(request):
    """Renders cart contents page"""
    return render(request, 'cart.html')


def add_product_to_cart(request, product_id):
    """Add a quantity of a product to the cart"""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if product_id in cart:
        if cart[product_id] is not None:
            cart[product_id] = int(cart[product_id]) + quantity
    else:
        cart[product_id] = cart.get(product_id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('products'))


def add_auction_to_cart(request, auction_id):
    """Add the auction you have won to the cart"""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if auction_id in cart:
        if cart[auction_id] is not None:
            cart[auction_id] = int(cart[auction_id]) + quantity
    else:
        cart[auction_id] = cart.get(auction_id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('index'))


def adjust_cart(request, id):
    """Adjust quantity of the selected product"""

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
