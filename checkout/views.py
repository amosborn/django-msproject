from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import OrderForm, MakePaymentForm
from .models import OrderLineItem
from products.models import Product
from lots.models import Auction
import stripe
from django.conf import settings
from django.utils import timezone
from django.contrib import messages

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout_cart(request):
    order_form = OrderForm(request.POST)
    payment_form = MakePaymentForm(request.POST)
    if request.method == 'POST':

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            cart = request.session.get('cart', {})
            total = 0

            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity
                )
                order_line_item.save()

                try:
                    customer = stripe.Charge.create(
                        amount=int(total * 100),
                        currency="EUR",
                        description=request.user.email,
                        card=payment_form.cleaned_data['stripe_id']
                        )
                except stripe.error.CardError:
                    messages.error(request, "Your card was declined")

                if customer.paid:
                    messages.error(request, "You have successfully paid")
                    request.session['cart'] = {}
                    return redirect(reverse('products'))
                else:
                    messages.error(request,
                                   "Unable to take payment with this card")

            else:
                print(payment_form.errors)
                messages.error(request,
                               "We were unable to take payment with this card")
        else:
            payment_form = MakePaymentForm()
            order_form = OrderForm()

    return render(request, "checkout.html",
                  {"order_form": order_form,
                   "payment_form": payment_form,
                   "publishable": settings.STRIPE_PUBLISHABLE
                   })


@login_required()
def checkout_auction(request, auction_id):
    order_form = OrderForm(request.POST)
    payment_form = MakePaymentForm(request.POST)
    auction = get_object_or_404(Auction, id=auction_id)
    total = auction.winning_bid
    auction.paid = True

    if request.method == 'POST':

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            order_line_item = OrderLineItem(
                order=order,
                auction=auction,
                quantity=1
            )
            order_line_item.save()
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                    )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined")

            if customer.paid:
                messages.error(request, "You have successfully paid")
                auction.save()
                return redirect(reverse('profile'))
            else:
                messages.error(request,
                               "Unable to take payment with this card")

        else:
            payment_form = MakePaymentForm()
            order_form = OrderForm()

    return render(request, "checkout.html",
                  {'auction': auction,
                   "order_form": order_form,
                   "payment_form": payment_form,
                   "publishable": settings.STRIPE_PUBLISHABLE
                   })
