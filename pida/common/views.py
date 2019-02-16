from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'notices': reverse('notice-list', request=request, format=format),
        'faqs': reverse('faq-list', request=request, format=format),
        'brands': reverse('brand-list', request=request, format=format),
        'products': reverse('product-list', request=request, format=format),
        'categories': reverse('category-list', request=request, format=format),
        'reviews': reverse('review-list', request=request, format=format),
        'group_purchase_events': reverse('grouppurchaseevent-list', request=request, format=format),
        'tester_orders': reverse('testerorder-list', request=request, format=format),
        'purchase_orders': reverse('purchaseorder-list', request=request, format=format),
        'group_purchase_orders': reverse('grouppurchaseorder-list', request=request, format=format),
    })
