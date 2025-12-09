@echo off
title Care Point System - Installation Wizard
color 0A

echo.
echo  ╔══════════════════════════════════════════════════════════════╗
echo  ║                    CARE POINT SYSTEM                         ║
echo  ║                  Installation Wizard                         ║
echo  ║                                                              ║
echo  ║              Healthcare Management System                    ║
echo  ╚══════════════════════════════════════════════════════════════╝
echo.
echo Welcome to the Care Point System installation wizard!
echo This script will help you set up the complete healthcare management system.
echo.

:main_menu
echo ========================================
echo Please select an option:
echo ========================================
echo.
echo 1. 🔍 Check system requirements
echo 2. 🐍 Install Python (if not installed)
echo 3. 🚀 Set up and run Care Point System
echo 4. ⚡ Quick start (if already set up)
echo 5. 🔧 Troubleshooting tools
echo 6. 📖 View setup instructions
echo 7. ❌ Exit
echo.
set /p choice="Enter your choice (1-7): "

if "%choice%"=="1" goto check_requirements
if "%choice%"=="2" goto install_python
if "%choice%"=="3" goto setup_system
if "%choice%"=="4" goto quick_start
if "%choice%"=="5" goto troubleshoot
if "%choice%"=="6" goto view_instructions
if "%choice%"=="7" goto exit
echo Invalid choice. Please try again.
goto main_menu

:check_requirements
echo.
echo Running system requirements check...
call check_requirements.bat
echo.
echo Press any key to return to main menu...
pause >nul
goto main_menu

:install_python
echo.
echo Starting Python installation...
call install_python.bat
echo.
echo Press any key to return to main menu...
pause >nul
goto main_menu

:setup_system
echo.
echo Starting Care Point System setup...
echo This will install all dependencies and set up the system.
echo.
call setup_and_run.bat
echo.
echo Press any key to return to main menu...
pause >nul
goto main_menu

:quick_start
echo.
echo Starting Care Point System (quick start)...
call quick_start.bat
echo.
echo Press any key to return to main menu...
pause >nul
goto main_menu

:troubleshoot
echo.
echo Opening troubleshooting tools...
call troubleshoot.bat
echo.
echo Press any key to return to main menu...
pause >nul
goto main_menu

:view_instructions
echo.
echo Opening setup instructions...
if exist "SETUP_INSTRUCTIONS.md" (
    notepad SETUP_INSTRUCTIONS.md
) else (
    echo Setup instructions file not found.
)
echo.
echo Press any key to return to main menu...
pause >nul
goto main_menu

:exit
echo.
echo Thank you for using Care Point System!
echo.
echo Quick reference for future use:
echo - Double-click START_HERE.bat to access this menu
echo - Double-click quick_start.bat to start the system quickly
echo - Check SETUP_INSTRUCTIONS.md for detailed documentation
echo.
echo Visit the project repository for updates and support.
echo.
pause
exit /b 0