@echo off
echo ========================================
echo Care Point System - Setup and Run Script
echo ========================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH!
    echo Please install Python 3.8+ from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo Python is installed. Checking version...
python --version

:: Check if pip is available
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: pip is not available!
    echo Please ensure pip is installed with Python
    pause
    exit /b 1
)

echo pip is available.
echo.

:: Get the directory where this batch file is located
set PROJECT_DIR=%~dp0
cd /d "%PROJECT_DIR%"

echo Current directory: %CD%
echo.

:: Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo ERROR: Failed to create virtual environment!
        pause
        exit /b 1
    )
    echo Virtual environment created successfully.
) else (
    echo Virtual environment already exists.
)

:: Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo ERROR: Failed to activate virtual environment!
    pause
    exit /b 1
)

echo Virtual environment activated.
echo.

:: Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

:: Install requirements
echo Installing project dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install requirements!
    echo Please check your internet connection and try again.
    pause
    exit /b 1
)

echo Dependencies installed successfully.
echo.

:: Check if .env file exists, if not create from example
if not exist ".env" (
    echo Creating .env file from example...
    if exist ".env.example" (
        copy ".env.example" ".env"
        echo.
        echo IMPORTANT: Please edit the .env file with your actual credentials:
        echo - Set DEBUG=True for development
        echo - Generate a SECRET_KEY
        echo - Configure email settings if needed
        echo - Configure payment gateway settings if needed
        echo.
        echo Opening .env file for editing...
        notepad .env
        echo.
        echo Please save and close the .env file, then press any key to continue...
        pause >nul
    ) else (
        echo Creating basic .env file...
        (
            echo # Django credentials
            echo DEBUG=True
            echo SECRET_KEY="django-insecure-change-this-key-in-production-123456789"
            echo.
            echo # Mailtrap credentials 
            echo SMTP_HOST='sandbox.smtp.mailtrap.io'
            echo SMTP_PORT=2525
            echo SMTP_USER='your_mailtrap_user'
            echo SMTP_PASSWORD='your_mailtrap_password'
            echo.
            echo # Payment Gateway (Offline) - SSL COMMERZ credentials 
            echo STORE_ID='your_store_id'
            echo STORE_PASSWORD='your_store_password'
            echo STORE_NAME='Care Point System'
        ) > .env
        echo Basic .env file created with default values.
    )
) else (
    echo .env file already exists.
)

echo.

:: Run Django migrations
echo Running database migrations...
python manage.py makemigrations
if %errorlevel% neq 0 (
    echo WARNING: makemigrations failed, but continuing...
)

python manage.py migrate
if %errorlevel% neq 0 (
    echo ERROR: Database migration failed!
    echo This might be due to database issues. Trying to continue...
)

echo Database setup completed.
echo.

:: Collect static files
echo Collecting static files...
python manage.py collectstatic --noinput
if %errorlevel% neq 0 (
    echo WARNING: collectstatic failed, but continuing...
)

echo.

:: Create superuser (optional)
echo.
echo ========================================
echo OPTIONAL: Create Django Admin Superuser
echo ========================================
set /p create_superuser="Do you want to create a superuser account? (y/n): "
if /i "%create_superuser%"=="y" (
    echo Creating superuser...
    python manage.py createsuperuser
)

echo.
echo ========================================
echo Setup Complete! Starting the server...
echo ========================================
echo.
echo The Care Point System will be available at:
echo http://127.0.0.1:8000/
echo.
echo Admin panel will be available at:
echo http://127.0.0.1:8000/admin/
echo.
echo Press Ctrl+C to stop the server
echo.

:: Start the Django development server
python manage.py runserver 127.0.0.1:8000

echo.
echo Server stopped.
echo.
echo To run the project again, simply double-click this batch file
echo or run: python manage.py runserver
echo.
pause