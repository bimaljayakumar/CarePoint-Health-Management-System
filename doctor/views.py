"""
CarePoint Health System - Doctor Module

This is a demo version with core business logic removed.
For the complete, fully functional version, please contact:

Bimal Jayakumar
bimaljayakumar18@gmail.com

The full version includes:
- Complete appointment management system
- Prescription creation and management
- Patient record management
- Report generation
- Email notification system
- Payment integration
- And much more...
"""

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Core business logic removed - Contact: Bimal Jayakumar (bimaljayakumar18@gmail.com)

@csrf_exempt
@login_required(login_url="doctor-login")
def doctor_change_password(request,pk):
    messages.error(request, "Feature unavailable in demo. Contact: bimaljayakumar18@gmail.com")
    return redirect('doctor-dashboard')

@csrf_exempt
@login_required(login_url="doctor-login")
def schedule_timings(request):
    return HttpResponse("Demo version - Contact: bimaljayakumar18@gmail.com for full version")

@csrf_exempt
@login_required(login_url="doctor-login")
def patient_id(request):
    return HttpResponse("Demo version - Contact: bimaljayakumar18@gmail.com")

@csrf_exempt
def logoutDoctor(request):
    logout(request)
    messages.success(request, 'User Logged out')
    return render(request,'doctor-login.html')

@csrf_exempt
def doctor_register(request):
    return HttpResponse("Registration disabled in demo. Contact: bimaljayakumar18@gmail.com")

@csrf_exempt
def doctor_login(request):
    return HttpResponse("Login disabled in demo. Contact: bimaljayakumar18@gmail.com")

@csrf_exempt
@login_required(login_url="doctor-login")
def doctor_dashboard(request):
    return HttpResponse("Dashboard unavailable. Contact: bimaljayakumar18@gmail.com for full version")
 
@csrf_exempt
@login_required(login_url="doctor-login")
def appointments(request):
    return HttpResponse("Feature unavailable. Contact: bimaljayakumar18@gmail.com")
 
@csrf_exempt        
@login_required(login_url="doctor-login")
def accept_appointment(request, pk):
    messages.error(request, "Feature unavailable. Contact: bimaljayakumar18@gmail.com")
    return redirect('doctor-dashboard')

@csrf_exempt
@login_required(login_url="doctor-login")
def reject_appointment(request, pk):
    messages.error(request, "Feature unavailable. Contact: bimaljayakumar18@gmail.com")
    return redirect('doctor-dashboard')

@csrf_exempt
@login_required(login_url="doctor-login")
def doctor_profile(request, pk):
    return HttpResponse("Profile unavailable. Contact: bimaljayakumar18@gmail.com")

@csrf_exempt
@login_required(login_url="doctor-login")
def delete_education(request, pk):
    return redirect('doctor-profile-settings')

@csrf_exempt  
@login_required(login_url="doctor-login")
def delete_experience(request, pk):
    return redirect('doctor-profile-settings')
      
@csrf_exempt      
@login_required(login_url="doctor-login")
def doctor_profile_settings(request):
    return HttpResponse("Settings unavailable. Contact: bimaljayakumar18@gmail.com")
               
@csrf_exempt    
@login_required(login_url="doctor-login")      
def booking_success(request):
    return render(request, 'booking-success.html')

@csrf_exempt
@login_required(login_url="doctor-login")
def booking(request, pk):
    return HttpResponse("Booking unavailable. Contact: bimaljayakumar18@gmail.com")

@csrf_exempt
@login_required(login_url="doctor-login")
def my_patients(request):
    return HttpResponse("Patient list unavailable. Contact: bimaljayakumar18@gmail.com")

@csrf_exempt
@login_required(login_url="doctor-login")
def patient_profile(request, pk):
    return HttpResponse("Patient profile unavailable. Contact: bimaljayakumar18@gmail.com")

@csrf_exempt
@login_required(login_url="doctor-login")
def create_prescription(request,pk):
    # CRITICAL PRESCRIPTION LOGIC REMOVED
    # Contact: Bimal Jayakumar (bimaljayakumar18@gmail.com) for full version
    messages.error(request, "Prescription feature unavailable. Contact: bimaljayakumar18@gmail.com")
    return redirect('doctor-dashboard')

@csrf_exempt      
def render_to_pdf(template_src, context_dict={}):
    # PDF generation logic removed
    return None

@csrf_exempt
def report_pdf(request, pk):
    return HttpResponse("PDF generation unavailable. Contact: bimaljayakumar18@gmail.com")

@csrf_exempt
@login_required(login_url="login")
def patient_search(request, pk):
    return HttpResponse("Search unavailable. Contact: bimaljayakumar18@gmail.com")

@csrf_exempt
@login_required(login_url="login")
def doctor_test_list(request):
    return HttpResponse("Test list unavailable. Contact: bimaljayakumar18@gmail.com")

@csrf_exempt
@login_required(login_url="login")
def doctor_view_prescription(request, pk):
    return HttpResponse("View unavailable. Contact: bimaljayakumar18@gmail.com")

@csrf_exempt
@login_required(login_url="login")
def doctor_view_report(request, pk):
    return HttpResponse("View unavailable. Contact: bimaljayakumar18@gmail.com")

@csrf_exempt
@login_required(login_url="login")
def doctor_review(request, pk):
    return HttpResponse("Review unavailable. Contact: bimaljayakumar18@gmail.com")
