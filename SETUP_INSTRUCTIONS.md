# Care Point System - Setup Instructions for Windows

## Prerequisites

Before running the setup, ensure you have:

1. **Python 3.8 or higher** installed from [python.org](https://www.python.org/downloads/)
   - ⚠️ **IMPORTANT**: During installation, check "Add Python to PATH"
   - Verify installation by opening Command Prompt and typing: `python --version`

2. **Internet connection** for downloading dependencies

## Quick Setup (Recommended)

### Option 1: Automatic Setup
1. Double-click `setup_and_run.bat`
2. Follow the on-screen instructions
3. The script will automatically:
   - Create a virtual environment
   - Install all dependencies
   - Set up the database
   - Create configuration files
   - Start the server

### Option 2: Manual Setup
If the automatic setup doesn't work, follow these steps:

1. Open Command Prompt as Administrator
2. Navigate to the project directory:
   ```cmd
   cd "C:\path\to\Care-Point-System"
   ```
3. Create virtual environment:
   ```cmd
   python -m venv venv
   ```
4. Activate virtual environment:
   ```cmd
   venv\Scripts\activate
   ```
5. Install dependencies:
   ```cmd
   pip install -r requirements.txt
   ```
6. Set up environment variables:
   ```cmd
   copy .env.example .env
   ```
7. Edit `.env` file with your settings (see Configuration section below)
8. Run migrations:
   ```cmd
   python manage.py migrate
   ```
9. Start the server:
   ```cmd
   python manage.py runserver
   ```

## Configuration

### Environment Variables (.env file)

The system requires a `.env` file with the following variables:

```env
# Django Settings
DEBUG=True
SECRET_KEY="your-secret-key-here"

# Email Configuration (Optional - for notifications)
SMTP_HOST='sandbox.smtp.mailtrap.io'
SMTP_PORT=2525
SMTP_USER='your_mailtrap_user'
SMTP_PASSWORD='your_mailtrap_password'

# Payment Gateway (Optional - for payments)
STORE_ID='your_store_id'
STORE_PASSWORD='your_store_password'
STORE_NAME='Care Point System'
```

### Default Configuration
If you don't configure email or payment settings, the system will still work with basic functionality.

## Running the Application

### First Time Setup
- Run `setup_and_run.bat` - This will set up everything and start the server

### Subsequent Runs
- Run `quick_start.bat` - This will quickly start the server using existing setup

### Manual Start
```cmd
cd "C:\path\to\Care-Point-System"
venv\Scripts\activate
python manage.py runserver
```

## Accessing the Application

Once the server is running, open your web browser and go to:

- **Main Application**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## Default Admin Account

After setup, you can create an admin account by:
1. Running the setup script (it will prompt you)
2. Or manually: `python manage.py createsuperuser`

## System Features

The Care Point System includes:

- **Patient Management**: Registration, profiles, medical history
- **Doctor Management**: Doctor profiles, schedules, appointments
- **Hospital Administration**: Hospital management, staff management
- **Pharmacy**: Medicine inventory, prescriptions
- **Appointments**: Booking, scheduling, notifications
- **Reports**: Medical reports, prescriptions, invoices
- **Payment Integration**: SSL Commerce payment gateway
- **Chat System**: Real-time communication
- **Laboratory**: Test management, results

## Troubleshooting

### Common Issues

1. **Python not found**
   - Install Python from python.org
   - Make sure "Add to PATH" is checked during installation
   - Restart Command Prompt after installation

2. **Permission errors**
   - Run Command Prompt as Administrator
   - Check antivirus software isn't blocking the installation

3. **Port already in use**
   - Change port: `python manage.py runserver 8001`
   - Or kill existing process using the port

4. **Database errors**
   - Delete `db.sqlite3` file and run `python manage.py migrate` again

5. **Static files not loading**
   - Run: `python manage.py collectstatic`

### Getting Help

If you encounter issues:
1. Check the error messages in the Command Prompt
2. Ensure all prerequisites are installed
3. Try running the manual setup steps
4. Check that your antivirus isn't blocking Python or the project files

## File Structure

```
Care-Point-System/
├── setup_and_run.bat          # Main setup script
├── quick_start.bat             # Quick start script
├── requirements.txt            # Python dependencies
├── manage.py                   # Django management script
├── .env                        # Environment variables (created during setup)
├── db.sqlite3                  # Database (created during setup)
├── healthstack/                # Main Django project
├── hospital/                   # Hospital management app
├── doctor/                     # Doctor management app
├── pharmacy/                   # Pharmacy management app
├── static/                     # Static files (CSS, JS, images)
├── templates/                  # HTML templates
└── media/                      # User uploaded files
```

## Security Notes

- Change the SECRET_KEY in production
- Set DEBUG=False in production
- Use proper database in production (PostgreSQL, MySQL)
- Configure proper email settings for production
- Set up SSL/HTTPS for production deployment

## Support

For technical support or questions about the Care Point System, please refer to the project documentation or contact the development team.