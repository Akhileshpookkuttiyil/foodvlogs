from .models import *
from .views import *


def count(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            ct = cart_list.objects.filter(cart_id=c_id(request))
            cart_items = items.objects.filter(cart=ct[:1])
            for item in cart_items:
                item_count += item.quantity
        except cart_list.DoesNotEXist:
            item_count = 0
        return dict(count=item_count)