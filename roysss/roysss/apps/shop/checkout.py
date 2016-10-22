
from django.conf import settings

import stripe
stripe.api_key = settings.STRIPE['SECRET_KEY']

from roysss.apps.shop.models import (
    Item, StripeOrder, StripeCharge,
    )


def stripe_checkout(request, **kwargs):
    token = stripe.Token.retrieve(kwargs.pop('stripeToken', None))

    style_id = kwargs.pop('style_id', None)
    item = Item.objects.get(style__style_id=style_id)

    order = StripeOrder.objects.create(
        uuid=request.session['uuid'],
        email=kwargs['stripeEmail'],
        name=kwargs['stripeBillingName'],
        country_code=kwargs['stripeBillingAddressCountryCode'],
        city=kwargs['stripeBillingAddressCity'],
        address_line1=kwargs['stripeBillingAddressLine1'],
        state=kwargs['stripeBillingAddressState'],
        zipcode=kwargs['stripeBillingAddressZip']
        )

    order.orderitems_set.create(item=item, quantity=1)

    metadata = {
        'request_id': request.request_id,
        'uuid': request.session['uuid'],
        'email': kwargs['stripeEmail'],
        }

    charge = stripe.Charge.create(
        amount=order.orderitems_set.total(),
        currency='usd',
        description='Roysss Order #%s' % order.number,
        metadata=metadata,
        receipt_email=kwargs['stripeEmail'],
        source=token,
        statement_descriptor='Roysss Order #%s' % order.number,
        )

    charge.order = order
    StripeCharge.objects.create(charge_id=charge.id, stripe_order=charge.order)

    return charge
