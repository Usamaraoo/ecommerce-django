from django.shortcuts import render, redirect, reverse
from .models import Customer
import stripe

stripe.api_key = "sk_test_51HFYxlA4CqyyLqmjEjgR9B7Qp6dA0yFN1eMejjRzOVgoxlRxUhiDAOeStD7bmMDAtXKDHXGQw9mZc0dV1tiRyFKg001mQh1LG4"


def payment(request):
    customer = request.user.customer

    return render(request, 'store/Checkout.html.html', {'customer': customer})


def charge(request):
    if request.method == 'POST':
        a = request.POST['total']
        amount = int(a.split('.')[0])
        print('DATA', request.POST)
        customer = stripe.Customer.create(
            # using two types of getting form data from field
            email=request.POST['email'],
            name=request.POST.get('name'),
            source=request.POST.get('stripeToken')  # Source that going to be charged actually the credit card
            # stripeToken was the value that returned on post credit card check in console
        )
        charge = stripe.Charge.create(
            customer=customer,
            amount=amount * 100,
            currency='usd',
            description='Customer Bill'
        )
    return redirect(reverse('success', args=[amount]))


def success(request, args):
    amount = args
    return render(request, 'store/successpayment.html', {'amount': amount})
