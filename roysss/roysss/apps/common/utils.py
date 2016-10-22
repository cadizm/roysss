
import string
import random


ORDER_NUMBER_CORPUS = string.uppercase + string.digits


def pp_cents_to_dollars(amount):
    return "$%d" % (amount / 100.0)


def gen_order_number(size=8, tries=0):
    from roysss.apps.shop.models import StripeOrder

    N = [
        random.choice(ORDER_NUMBER_CORPUS)
        for _ in range(size)
    ]

    number = ''.join(N)

    try:
        StripeOrder.objects.get(number=number)
    except StripeOrder.DoesNotExist:
        return number

    if tries < 5:
        return gen_order_number(size=size, tries=tries+1)

    raise Exception("Couldn't generate order number")
