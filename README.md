# 🏥 CarePoint Health Management System (DEMO VERSION)

<div align="center">

![Django](https://img.shields.io/badge/Django-4.0+-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![License](https://img.shields.io/badge/License-Proprietary-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Demo-yellow?style=for-the-badge)

</div>

## ⚠️ IMPORTANT NOTICE

**THIS IS A DEMONSTRATION VERSION WITH LIMITED FUNCTIONALITY**

Core backend features including authentication, payment processing, and database operations have been intentionally removed. This version is for **evaluation and portfolio purposes only**.

### 📧 Contact for Full Project

**Developer:** Bimal Jayakumar  
**Email:** bimaljayakumar18@gmail.com  
**GitHub:** [@bimaljayakumar](https://github.com/bimaljayakumar)

💼 **Interested in the complete working project?** Contact me to purchase the full version with all features fully implemented and production-ready.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [System Architecture](#system-architecture)
- [Installation](#installation)
- [Configuration](#configuration)
- [Screenshots](#screenshots)
- [Demo Limitations](#demo-limitations)
- [Full Version Features](#full-version-features)
- [License](#license)
- [Contact](#contact)

---

## 🌟 Overview

![CarePoint Home](screenshots/127.0.0.1_8000_(HD).png)

**CarePoint Health Management System** is a comprehensive Django-based healthcare platform designed to revolutionize hospital operations and medical service delivery. This full-stack web application provides an integrated digital ecosystem for healthcare providers, patients, administrative staff, laboratory technicians, and pharmacists.

**⚠️ Note:** This demo version showcases the UI/UX and frontend functionality. Backend features like authentication, payment processing, and email notifications are not functional in this version.

### Mission Statement
**"Digitizing Hospital Operations | Streamlining Medical Service Delivery"**

### Key Objectives
- Provide seamless appointment management
- Enable digital prescription workflows
- Facilitate laboratory test management
- Streamline pharmacy operations
- Centralize medical records
- Integrate payment processing

---

## ✨ Features

**⚠️ DEMO VERSION NOTICE:** The features listed below represent the full project design. In this demo version, only frontend UI/UX is functional. Backend operations are not implemented.

### 👨⚕️ Doctor Portal

- **Appointment Management** - View, accept, reject appointments with calendar *(UI only in demo)*
- **Digital Prescriptions** - Create detailed prescriptions with medicines and tests *(Not functional in demo)*
- **Patient Records** - Access complete patient medical history *(UI only)*
- **Medical Reports** - Generate and manage laboratory reports *(Not functional in demo)*
- **Real-time Chat** - Communicate with patients instantly *(Not functional in demo)*
- **Dashboard Analytics** - Revenue tracking, patient statistics *(Frontend only)*
- **Profile Management** - Update qualifications, experience, availability *(UI only)*
- **Schedule Management** - Set visiting hours and availability *(Frontend only)*

### 👤 Patient Portal

- **Online Booking** - Book appointments with preferred doctors *(Not functional in demo)*
- **Doctor Search** - Filter by specialization, hospital, availability *(Frontend only)*
- **Medical History** - View all past prescriptions and reports *(UI only)*
- **Prescription Downloads** - Download prescriptions as PDF *(Not functional in demo)*
- **Online Pharmacy** - Order medicines with prescription validation *(Not functional in demo)*
- **Lab Tests** - Book tests, view results, download reports *(Not functional in demo)*
- **Payment Processing** - Secure online payments for services *(Not functional in demo)*
- **Profile Management** - Update personal and medical information *(UI only)*

### 🏢 Hospital Admin Portal

- **Doctor Approval** - Review and approve doctor registrations *(Not functional in demo)*
- **Hospital Management** - Add/edit hospitals, departments, specializations *(UI only)*
- **Staff Management** - Manage lab workers and pharmacists *(UI only)*
- **System Analytics** - Comprehensive reports and statistics *(Frontend only)*
- **Revenue Tracking** - Monitor financial performance *(Not functional in demo)*
- **User Management** - Manage all system users *(Not functional in demo)*
- **Department Setup** - Configure hospital departments and services *(UI only)*
- **Emergency Information** - Manage emergency contact details *(UI only)*

### 🔬 Lab Worker Portal

- **Test Management** - Manage laboratory test catalog *(UI only)*
- **Order Processing** - Process test orders from prescriptions *(Not functional in demo)*
- **Report Generation** - Create detailed medical reports *(Not functional in demo)*
- **Result Upload** - Upload test results with specimen details *(Not functional in demo)*
- **Email Delivery** - Automated report delivery to patients *(Not functional in demo)*
- **Patient Management** - View patient test history *(UI only)*
- **Dashboard** - Track pending and completed tests *(Frontend only)*

### 💊 Pharmacist Portal

- **Medicine Inventory** - Complete medicine catalog management *(UI only)*
- **Stock Management** - Track medicine quantities and availability *(UI only)*
- **Order Processing** - Process prescription orders *(Not functional in demo)*
- **Sales Analytics** - Revenue and sales statistics *(Frontend only)*
- **Medicine Categories** - Organize by type, category, prescription requirement *(UI only)*
- **Order Fulfillment** - Manage order status and delivery *(Not functional in demo)*
- **Dashboard** - Monitor inventory and sales *(Frontend only)*

---

## 🛠️ Technology Stack

### Backend Technologies
```
- Python 3.8+
- Django 4.0+ (Web Framework)
- Django REST Framework (API)
- SQLite (Development Database)
- PostgreSQL (Production - Full Version)
```

### Frontend Technologies
```
- HTML5 (Semantic Markup)
- CSS3 (Styling & Animations)
- JavaScript ES6+ (Interactivity)
- Bootstrap 5 (Responsive Framework)
- jQuery (DOM Manipulation)
- AJAX (Asynchronous Operations)
```

### Integrations & Libraries
```
- SSLCommerz (Payment Gateway - Full Version Only)
- xhtml2pdf (PDF Generation)
- SMTP (Email Service)
- Chart.js (Data Visualization)
- Select2 (Enhanced Dropdowns)
- DataTables (Table Management)
- Django Channels (WebSocket - Full Version)
```

### Security & Privacy
```
- CSRF Protection
- SQL Injection Prevention
- XSS Protection
- Password Hashing (PBKDF2)
- Session Security
- File Upload Validation
- Role-based Access Control
```

---

## 🏗️ System Architecture

### Project Structure
```
CarePoint-Health-Management-System/
├── doctor/                      # Doctor Module
│   ├── models.py               # Doctor, Appointment, Prescription models
│   ├── views.py                # Doctor dashboard, patient management
│   ├── forms.py                # Doctor registration, profile forms
│   ├── urls.py                 # Doctor URL routing
│   └── migrations/             # Database migrations
├── hospital/                    # Patient & Hospital Module
│   ├── models.py               # Patient, Hospital, User models
│   ├── views.py                # Patient dashboard, booking system
│   ├── forms.py                # Patient registration, profile forms
│   ├── urls.py                 # Patient URL routing
│   └── migrations/             # Database migrations
├── hospital_admin/              # Admin Module
│   ├── models.py               # Admin, Lab Worker, Test models
│   ├── views.py                # Admin dashboard, management
│   ├── forms.py                # Admin forms
│   ├── urls.py                 # Admin URL routing
│   └── migrations/             # Database migrations
├── pharmacy/                    # Pharmacy Module
│   ├── models.py               # Medicine, Cart, Order models
│   ├── views.py                # Pharmacy shop, inventory
│   ├── forms.py                # Medicine forms
│   ├── urls.py                 # Pharmacy URL routing
│   └── migrations/             # Database migrations
├── sslcommerz/                  # Payment Gateway Module (Full Version)
│   ├── models.py               # Payment transaction models
│   ├── views.py                # Payment processing
│   ├── urls.py                 # Payment URL routing
│   └── migrations/             # Database migrations
├── api/                         # REST API Module
│   ├── views.py                # API endpoints
│   ├── serializers.py          # Data serializers
│   └── urls.py                 # API URL routing
├── ChatApp/                     # Real-time Chat Module
│   ├── models.py               # Chat models
│   ├── views.py                # Chat functionality
│   └── urls.py                 # Chat URL routing
├── templates/                   # HTML Templates
│   ├── doctor/                 # Doctor templates
│   ├── hospital_admin/         # Admin templates
│   ├── Pharmacy/               # Pharmacy templates
│   └── *.html                  # Common templates
├── static/                      # Static Files
│   ├── css/                    # Stylesheets
│   ├── js/                     # JavaScript files
│   └── images/                 # Images
├── media/                       # User Uploads
│   ├── doctors/                # Doctor images
│   ├── patients/               # Patient images
│   └── medicines/              # Medicine images
├── screenshots/                 # Project Screenshots
├── healthstack/                 # Project Configuration
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main URL configuration
│   └── wsgi.py                 # WSGI configuration
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

## 📦 Installation

### Prerequisites

**Required Software:**
- Python 3.8 or higher ([Download](https://www.python.org/downloads/))
- pip (Python package manager)
- Git ([Download](https://git-scm.com/))
- Modern web browser (Chrome, Firefox, Safari)

### Step-by-Step Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/bimaljayakumar/CarePoint-Health-Management-System.git
cd CarePoint-Health-Management-System
```

#### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Note:** This demo version has minimal dependencies. Full version includes additional packages for payment processing, email services, and real-time features.

#### 4. Database Setup
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

#### 5. Run Development Server
```bash
python manage.py runserver
```

#### 6. Access Application
- **Main Site:** http://127.0.0.1:8000
- **Admin Panel:** http://127.0.0.1:8000/admin

**⚠️ Demo Limitation:** Most features will display UI only. Backend functionality is not available in this version.

---

## ⚙️ Configuration

### Django Settings (Demo Version)

**settings.py Configuration:**

```python
# Security
SECRET_KEY = 'demo-key-removed'
DEBUG = False
ALLOWED_HOSTS = []

# Database (Demo - No configuration)
DATABASES = {}

# Email Configuration (Removed in Demo)
# Full version includes SMTP configuration

# Payment Gateway (Removed in Demo)
# Full version includes SSLCommerz integration

# Static Files
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
```

**⚠️ Note:** All sensitive configurations have been removed from this demo version. Contact for full version with complete configuration.

---

## 📸 Screenshots

### 🏠 Home & Authentication

<div align="center">

#### Home Page
![Home Page](screenshots/127.0.0.1_8000_(HD).png)

</div>

<table>
  <tr>
    <td><img src="screenshots/127.0.0.1_8000_login_(HD).png" alt="Login" width="400"/><br/><b>Login System</b></td>
    <td><img src="screenshots/127.0.0.1_8000_about-us_(HD).png" alt="About Us" width="400"/><br/><b>About Us</b></td>
  </tr>
</table>

### 👤 Patient Portal

<table>
  <tr>
    <td><img src="screenshots/127.0.0.1_8000_patient-dashboard_(HD).png" alt="Patient Dashboard" width="400"/><br/><b>Patient Dashboard</b></td>
    <td><img src="screenshots/127.0.0.1_8000_search_(HD).png" alt="Doctor Search" width="400"/><br/><b>Doctor Search & Filter</b></td>
  </tr>
  <tr>
    <td><img src="screenshots/127.0.0.1_8000_multiple-hospital_(HD).png" alt="Hospitals" width="400"/><br/><b>Hospital Listing</b></td>
    <td><img src="screenshots/127.0.0.1_8000_pharmacy_shop_(HD).png" alt="Pharmacy" width="400"/><br/><b>Online Pharmacy</b></td>
  </tr>
  <tr>
    <td><img src="screenshots/127.0.0.1_8000_profile-settings_(HD).png" alt="Profile" width="400"/><br/><b>Profile Settings</b></td>
    <td><img src="screenshots/127.0.0.1_8000_change-password_45(HD).png" alt="Change Password" width="400"/><br/><b>Change Password</b></td>
  </tr>
</table>

### 👨⚕️ Doctor Portal

<table>
  <tr>
    <td><img src="screenshots/127.0.0.1_8000_doctor_doctor-dashboard_(HD).png" alt="Doctor Dashboard" width="400"/><br/><b>Doctor Dashboard</b></td>
    <td><img src="screenshots/127.0.0.1_8000_doctor_my-patients_(HD).png" alt="My Patients" width="400"/><br/><b>Patient Management</b></td>
  </tr>
  <tr>
    <td><img src="screenshots/127.0.0.1_8000_doctor_doctor-profile_11_(HD).png" alt="Doctor Profile" width="400"/><br/><b>Doctor Profile</b></td>
    <td><img src="screenshots/127.0.0.1_8000_doctor_(HD).png" alt="Doctor Login" width="400"/><br/><b>Doctor Login</b></td>
  </tr>
</table>

### 🏢 Hospital Admin Portal

<table>
  <tr>
    <td><img src="screenshots/127.0.0.1_8000_hospital_admin_admin-dashboard_(HD).png" alt="Admin Dashboard" width="400"/><br/><b>Admin Dashboard</b></td>
    <td><img src="screenshots/127.0.0.1_8000_hospital_admin_medicine-list_(HD).png" alt="Medicine List" width="400"/><br/><b>Medicine Management</b></td>
  </tr>
  <tr>
    <td><img src="screenshots/127.0.0.1_8000_hospital_admin_add-medicine_(HD).png" alt="Add Medicine" width="400"/><br/><b>Add Medicine</b></td>
    <td><img src="screenshots/127.0.0.1_8000_hospital_admin_test-list_(HD).png" alt="Test List" width="400"/><br/><b>Lab Test Management</b></td>
  </tr>
  <tr>
    <td><img src="screenshots/127.0.0.1_8000_hospital_admin_(HD).png" alt="Admin Login" width="400"/><br/><b>Admin Login</b></td>
    <td><img src="screenshots/127.0.0.1_8000_hospital_admin_mypatient-list_(HD).png" alt="Patient List" width="400"/><br/><b>Patient List</b></td>
  </tr>
</table>

### 🔬 Lab Worker & 💊 Pharmacist Portals

<table>
  <tr>
    <td><img src="screenshots/127.0.0.1_8000_hospital_admin_labworker-dashboard_(HD).png" alt="Lab Dashboard" width="400"/><br/><b>Lab Worker Dashboard</b></td>
    <td><img src="screenshots/127.0.0.1_8000_hospital_admin_pharmacist-dashboard_(HD).png" alt="Pharmacist Dashboard" width="400"/><br/><b>Pharmacist Dashboard</b></td>
  </tr>
</table>

---

## ⚠️ Demo Limitations

### Removed Features (Demo Version)

❌ **Backend Features:**
- Authentication and login system
- Appointment booking algorithms
- Prescription creation logic
- Payment gateway integration (SSLCommerz)
- Report generation and PDF export
- Email notification system
- SMS integration
- Real-time chat functionality
- Database operations for critical features
- All business logic and validations

❌ **Security Features:**
- Production-grade encryption
- Advanced authentication mechanisms
- Rate limiting
- Session management logic
- API authentication

❌ **Integration Features:**
- Payment processing (SSLCommerz)
- Email delivery (SMTP)
- SMS alerts
- Third-party APIs
- WebSocket for real-time chat

❌ **Configuration:**
- Database connection settings
- Email server configuration
- Payment gateway credentials
- Secret keys and tokens
- Production settings

### Available Features (Demo Version)

✅ **Frontend Features:**
- Complete UI/UX design
- Responsive layouts
- Interactive dashboards
- Form interfaces
- Navigation systems
- Static content display
- CSS animations and styling

✅ **Basic Structure:**
- Database models structure (no data operations)
- URL routing (non-functional)
- Template rendering
- Static file serving
- Project architecture

---

## 🎯 Full Version Features

### Complete Backend Implementation
- ✅ Fully functional authentication system
- ✅ Complete appointment management with scheduling
- ✅ Prescription creation and management
- ✅ Payment gateway integration (SSLCommerz)
- ✅ PDF generation for prescriptions and reports
- ✅ Email notification system (SMTP)
- ✅ SMS alert integration
- ✅ Real-time chat with WebSocket (Django Channels)
- ✅ Advanced search and filtering algorithms
- ✅ Complete database operations

### Production-Ready Features
- ✅ PostgreSQL database
- ✅ Redis caching
- ✅ Celery task queue for async operations
- ✅ AWS S3 storage for media files
- ✅ CDN integration
- ✅ Load balancing configuration
- ✅ Auto-scaling setup

### Security Enhancements
- ✅ SSL/TLS certificates
- ✅ Advanced encryption for sensitive data
- ✅ Rate limiting and throttling
- ✅ DDoS protection
- ✅ Security auditing and logging
- ✅ HIPAA compliance features
- ✅ Two-factor authentication

### Additional Features
- ✅ Multi-language support (i18n)
- ✅ Mobile app integration (REST API)
- ✅ Voice commands for accessibility
- ✅ Telemedicine video consultation
- ✅ Insurance claim integration
- ✅ Advanced analytics dashboard
- ✅ Comprehensive reporting system
- ✅ Automated backup system

### Documentation & Support
- ✅ Complete API documentation
- ✅ Deployment guides (AWS, Heroku, DigitalOcean)
- ✅ User manuals for all roles
- ✅ Admin configuration guides
- ✅ Video tutorials
- ✅ Technical support (30 days)
- ✅ Bug fixes and updates (6 months)

---

## 📄 License

**Proprietary License**

© 2024 Bimal Jayakumar. All Rights Reserved.

This is a demonstration version with restricted usage:
- ❌ No commercial use
- ❌ No redistribution
- ❌ No modification
- ✅ Evaluation purposes only

See [LICENSE.md](LICENSE.md) for full terms.

---

## 📞 Contact

### Developer Information

**Bimal Jayakumar**

📧 **Email:** bimaljayakumar18@gmail.com  
🐙 **GitHub:** [@bimaljayakumar](https://github.com/bimaljayakumar)  
💼 **LinkedIn:** [Connect with me](https://linkedin.com/in/bimaljayakumar)

### Purchase Full Version

Interested in the complete working project?

**What You Get:**
- ✅ Complete source code with all features
- ✅ Full backend implementation
- ✅ Production-ready deployment configuration
- ✅ Complete documentation and guides
- ✅ Technical support (30 days)
- ✅ Free updates and bug fixes (6 months)
- ✅ Customization assistance
- ✅ Deployment support

**Payment Methods:**

<div align="center">

![Google Pay](screenshots/GooglePay_QR.png)

*Scan to pay via Google Pay/UPI*

</div>

**Payment Methods:**

<div align="center">

![Google Pay](screenshots/GooglePay_QR.png)

*Scan to pay via Google Pay/UPI*

</div>

**Contact:** bimaljayakumar18@gmail.com

---

## 🙏 Acknowledgments

- Django Framework Team
- Python Community
- Open Source Contributors
- Healthcare Technology Advocates

---

## 📊 Project Stats

- **Lines of Code:** 20,000+
- **Files:** 671
- **Apps:** 7
- **Models:** 25+
- **Views:** 80+
- **Templates:** 100+
- **Screenshots:** 25

---

<div align="center">

**Made with 💙 for healthcare digitization and patient care**

© 2024 Bimal Jayakumar. All Rights Reserved.

[⬆ Back to Top](#-carepoint-health-management-system-demo-version)

</div>
