"""
CarePoint Health System - Doctor Models

This is a demo version with database models intact but business logic removed.
For the complete, fully functional version, please contact:

Bimal Jayakumar
bimaljayakumar18@gmail.com
"""

from django.db import models
import uuid
from hospital.models import Hospital_Information, User, Patient
from hospital_admin.models import hospital_department, specialization, service
from django.conf import settings

# Models are kept for database structure reference
# Business logic and complex methods have been removed

class BannerVideo(models.Model):
    title = models.CharField(max_length=200, default="Welcome To Care Point")
    subtitle = models.CharField(max_length=200, default="Choose well by choosing us.")
    video_file = models.FileField(upload_to='banner_videos/', help_text="Upload MP4 video file")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Banner Video"
        verbose_name_plural = "Banner Videos"
    
    def __str__(self):
        return self.title

class Doctor_Information(models.Model):
    DOCTOR_TYPE = (
        ('Cardiologists', 'Cardiologists'),
        ('Neurologists', 'Neurologists'),
        ('Pediatricians', 'Pediatricians'),
        ('Physiatrists', 'Physiatrists'),
        ('Dermatologists', 'Dermatologists'),
    )
    
    doctor_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='profile')
    name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    department = models.CharField(max_length=200, choices=DOCTOR_TYPE, null=True, blank=True)
    department_name = models.ForeignKey(hospital_department, on_delete=models.SET_NULL, null=True, blank=True)
    specialization = models.ForeignKey(specialization, on_delete=models.SET_NULL, null=True, blank=True)
    featured_image = models.ImageField(upload_to='doctors/', default='doctors/user-default.png', null=True, blank=True)
    certificate_image = models.ImageField(upload_to='doctors_certificate/', default='doctors_certificate/default.png', null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=200, null=True, blank=True)
    nid = models.CharField(max_length=200, null=True, blank=True)
    visiting_hour = models.CharField(max_length=200, null=True, blank=True)
    consultation_fee = models.IntegerField(null=True, blank=True)
    report_fee = models.IntegerField(null=True, blank=True)
    dob = models.CharField(max_length=200, null=True, blank=True)
    institute = models.CharField(max_length=200, null=True, blank=True)
    degree = models.CharField(max_length=200, null=True, blank=True)
    completion_year = models.CharField(max_length=200, null=True, blank=True)
    work_place = models.CharField(max_length=200, null=True, blank=True)
    designation = models.CharField(max_length=200, null=True, blank=True)
    start_year = models.CharField(max_length=200, null=True, blank=True)
    end_year = models.CharField(max_length=200, null=True, blank=True)
    register_status =  models.CharField(max_length=200, null=True, blank=True)
    hospital_name = models.ForeignKey(Hospital_Information, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)

class Appointment(models.Model):
    APPOINTMENT_TYPE = (
        ('report', 'report'),
        ('checkup', 'checkup'),
    )
    APPOINTMENT_STATUS = (
        ('pending', 'pending'),
        ('confirmed', 'confirmed'),
        ('cancelled', 'cancelled'),
    )

    id = models.AutoField(primary_key=True)
    date = models.DateField(null=True, blank=True)
    time = models.CharField(max_length=200, null=True, blank=True)
    doctor = models.ForeignKey(Doctor_Information, on_delete=models.CASCADE, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    appointment_type = models.CharField(max_length=200, choices=APPOINTMENT_TYPE)
    appointment_status = models.CharField(max_length=200, choices=APPOINTMENT_STATUS)
    serial_number = models.CharField(max_length=200, null=True, blank=True)
    payment_status = models.CharField(max_length=200, null=True, blank=True, default='pending')
    transaction_id = models.CharField(max_length=255, null=True, blank=True)
    message = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.patient.username)

class Education(models.Model):
    education_id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor_Information, on_delete=models.CASCADE, null=True, blank=True)
    degree = models.CharField(max_length=200, null=True, blank=True)
    institute = models.CharField(max_length=200, null=True, blank=True)
    year_of_completion = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return str(self.doctor.name)
    
class Experience(models.Model):
    experience_id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor_Information, on_delete=models.CASCADE, null=True, blank=True)
    work_place_name = models.CharField(max_length=200, null=True, blank=True)
    from_year = models.CharField(max_length=200, null=True, blank=True)
    to_year = models.CharField(max_length=200, null=True, blank=True)
    designation = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return str(self.doctor.name)

class Report(models.Model):
    report_id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor_Information, on_delete=models.SET_NULL, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    specimen_id = models.CharField(max_length=200, null=True, blank=True)
    specimen_type = models.CharField(max_length=200, null=True, blank=True)
    collection_date = models.CharField(max_length=200, null=True, blank=True)
    receiving_date = models.CharField(max_length=200, null=True, blank=True)
    test_name = models.CharField(max_length=200, null=True, blank=True)
    result = models.CharField(max_length=200, null=True, blank=True)
    unit = models.CharField(max_length=200, null=True, blank=True)
    referred_value = models.CharField(max_length=200, null=True, blank=True)
    delivery_date = models.CharField(max_length=200, null=True, blank=True)
    other_information = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.patient.username)

class Specimen(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE, null=True, blank=True)
    specimen_id = models.AutoField(primary_key=True)
    specimen_type = models.CharField(max_length=200, null=True, blank=True)
    collection_date = models.CharField(max_length=200, null=True, blank=True)
    receiving_date = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return str(self.report.report_id)

class Test(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE, null=True, blank=True)
    test_id = models.AutoField(primary_key=True)
    test_name = models.CharField(max_length=200, null=True, blank=True)
    result = models.CharField(max_length=200, null=True, blank=True)
    unit = models.CharField(max_length=200, null=True, blank=True)
    referred_value = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return str(self.report.report_id)
        
class Prescription(models.Model):
    prescription_id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor_Information, on_delete=models.CASCADE, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True, blank=True)
    create_date = models.CharField(max_length=200, null=True, blank=True)
    medicine_name = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.CharField(max_length=200, null=True, blank=True)
    days = models.CharField(max_length=200, null=True, blank=True)
    time = models.CharField(max_length=200, null=True, blank=True)
    relation_with_meal = models.CharField(max_length=200, null=True, blank=True)
    medicine_description = models.TextField(null=True, blank=True)
    test_name = models.CharField(max_length=200, null=True, blank=True)
    test_description = models.TextField(null=True, blank=True)
    extra_information = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.patient:
            return str(self.patient.username)
        return f"Prescription {self.prescription_id}"

class Prescription_medicine(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, null=True, blank=True)
    medicine_id = models.AutoField(primary_key=True)
    medicine_name = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.CharField(max_length=200, null=True, blank=True)
    duration = models.CharField(max_length=200, null=True, blank=True)
    frequency = models.CharField(max_length=200, null=True, blank=True)
    relation_with_meal = models.CharField(max_length=200, null=True, blank=True)
    instruction = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.prescription.prescription_id)

class Prescription_test(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, null=True, blank=True)
    test_id = models.AutoField(primary_key=True)
    test_name = models.CharField(max_length=200, null=True, blank=True)
    test_description = models.TextField(null=True, blank=True)
    test_info_id = models.CharField(max_length=200, null=True, blank=True)
    test_info_price = models.CharField(max_length=200, null=True, blank=True)
    test_info_pay_status = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        if self.prescription:
            return str(self.prescription.prescription_id)
        return f"Test {self.test_id}"
    
class testCart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='test_cart')
    item = models.ForeignKey(Prescription_test, on_delete=models.CASCADE)
    name = models.CharField(default='test', max_length=200)
    purchased = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.item.test_info_id} X {self.item.test_name}'

    # Business logic removed - Contact: bimaljayakumar18@gmail.com

class testOrder(models.Model):
    orderitems = models.ManyToManyField(testCart)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=200, blank=True, null=True)
    trans_ID = models.CharField(max_length=200, blank=True, null=True)

    # Business logic removed - Contact: bimaljayakumar18@gmail.com

class Doctor_review(models.Model):
    review_id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor_Information, on_delete=models.CASCADE, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    message = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.patient.username)
