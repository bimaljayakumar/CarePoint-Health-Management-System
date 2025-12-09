"""
CarePoint Health System - Pharmacy Module

This is a demo version with core business logic removed.
For the complete, fully functional version, please contact:

Bimal Jayakumar
bimaljayakumar18@gmail.com

The full version includes:
- Complete pharmacy management system
- Medicine inventory and ordering
- Shopping cart functionality
- Payment integration
- Order tracking
- And much more...
"""

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Core business logic removed - Contact: Bimal Jayakumar (bimaljayakumar18@gmail.com)

@csrf_exempt
@login_required(login_url="login")
def shop(request):
    return HttpResponse("Pharmacy shop unavailable. Contact: bimaljayakumar18@gmail.com")

@csrf_exempt
@login_required(login_url="login")
def product_single(request, pk):
    return HttpResponse("Product view unavailable. Contact: bimaljayakumar18@gmail.com")

@csrf_exempt
@login_required(login_url="login")
def add_to_cart(request, pk):
    return HttpResponse("Cart unavailable. Contact: bimaljayakumar18@gmail.com")

@csrf_exempt
@login_required(login_url="login")
def cart(request):
    return HttpResponse("Cart unavailable. Contact: bimaljayakumar18@gmail.com")

@csrf_exempt
@login_required(login_url="login")
def remove_from_cart(request, pk):
    return HttpResponse("Cart unavailable. Contact: bimaljayakumar18@gmail.com")

@csrf_exempt
@login_required(login_url="login")
def checkout(request):
    return HttpResponse("Checkout unavailable. Contact: bimaljayakumar18@gmail.com")
