
from django.contrib.auth.models import Permission
from django.conf import settings
from django.views.generic.base import TemplateView
from django.shortcuts import render
import stripe


stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context
# Create your views here.

def charge(request): # new
    # Get the permission
    permission = Permission.objects.get(codename='special_status')

    # Get user
    u = request.user
    
    # Add to user's permission set
    u.user_permissions.add(permission)

    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=3900,
            currency='usd',
            description='Purchase all books',
            source=request.POST['stripeToken']
    )

    return render(request, 'orders/charge.html')