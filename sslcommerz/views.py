"""
CarePoint Health System - Payment Module

This is a demo version with core business logic removed.
For the complete, fully functional version, please contact:

Bimal Jayakumar
bimaljayakumar18@gmail.com

The full version includes:
- Complete payment gateway integration
- SSLCommerz payment processing
- Transaction management
- Payment verification
- Order processing
- And much more...
"""

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Core payment logic removed - Contact: Bimal Jayakumar (bimaljayakumar18@gmail.com)

@csrf_exempt
@login_required(login_url="login")
def payment_index(request):
    return HttpResponse("Payment unavailable. Contact: bimaljayakumar18@gmail.com")

@csrf_exempt
@login_required(login_url="login")
def checkout(request):
    return HttpResponse("Checkout unavailable. Contact: bimaljayakumar18@gmail.com")

@csrf_exempt
def success(request):
    return HttpResponse("Payment processing unavailable. Contact: bimaljayakumar18@gmail.com")

@csrf_exempt
def fail(request):
    return HttpResponse("Payment processing unavailable. Contact: bimaljayakumar18@gmail.com")

@csrf_exempt
def cancel(request):
    return HttpResponse("Payment processing unavailable. Contact: bimaljayakumar18@gmail.com")

@csrf_exempt
def ipn(request):
    return HttpResponse("IPN unavailable. Contact: bimaljayakumar18@gmail.com")
