@echo off
echo ========================================
echo Care Point System - Quick Start
echo ========================================
echo.

:: Get the directory where this batch file is located
set PROJECT_DIR=%~dp0
cd /d "%PROJECT_DIR%"

:: Check if virtual environment exists
if not exist "venv" (
    echo ERROR: Virtual environment not found!
    echo Please run setup_and_run.bat first to set up the project.
    pause
    exit /b 1
)

:: Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Starting Care Point System...
echo.
echo The application will be available at:
echo http://127.0.0.1:8000/
echo.
echo Press Ctrl+C to stop the server
echo.

:: Start the Django development server
python manage.py runserver 127.0.0.1:8000

echo.
echo Server stopped.
pause