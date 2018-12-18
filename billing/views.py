from django.shortcuts import render
import stripe

stripe.api_key = "sk_test_sfV52hBYwCO5Jtvu9NRtJTlt"
STRIPE_PUB_KEY = 'pk_test_Jqmc6mRzEWuEynf8ObY5J90c'


def payment_method_view(request):
    if request.method == "POST":
        print(request.POST)
    return render(request, 'billing/payment-method.html', {"publish_key": STRIPE_PUB_KEY})
