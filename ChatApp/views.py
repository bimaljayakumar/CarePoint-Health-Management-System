"""
CarePoint Health System - Chat Module

This is a demo version with core business logic removed.
For the complete, fully functional version, please contact:

Bimal Jayakumar
bimaljayakumar18@gmail.com

The full version includes:
- Real-time chat functionality
- WebSocket integration
- Message history
- User presence tracking
- And much more...
"""

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Core chat logic removed - Contact: Bimal Jayakumar (bimaljayakumar18@gmail.com)

@csrf_exempt
@login_required(login_url="login")
def chat_home(request):
    return HttpResponse("Chat unavailable. Contact: bimaljayakumar18@gmail.com for full version")

@csrf_exempt
@login_required(login_url="login")
def chat_room(request, room_name):
    return HttpResponse("Chat room unavailable. Contact: bimaljayakumar18@gmail.com")
