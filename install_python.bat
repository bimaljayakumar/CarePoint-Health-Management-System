@echo off
echo ========================================
echo Python Installer for Care Point System
echo ========================================
echo.

:: Check if Python is already installed
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Python is already installed:
    python --version
    echo.
    echo You can now run setup_and_run.bat to set up the Care Point System.
    pause
    exit /b 0
)

echo Python is not installed on this system.
echo.
echo This script will help you install Python 3.11.
echo.
set /p install_python="Do you want to download and install Python? (y/n): "
if /i not "%install_python%"=="y" (
    echo Installation cancelled.
    echo Please install Python manually from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo.
echo Downloading Python 3.11 installer...
echo This may take a few minutes depending on your internet connection.
echo.

:: Create temp directory
if not exist "temp" mkdir temp

:: Download Python installer
powershell -Command "& {Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.11.7/python-3.11.7-amd64.exe' -OutFile 'temp\python-installer.exe'}"

if not exist "temp\python-installer.exe" (
    echo ERROR: Failed to download Python installer.
    echo Please check your internet connection and try again.
    echo Alternatively, download Python manually from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo.
echo Download completed. Starting installation...
echo.
echo IMPORTANT: During installation, make sure to:
echo 1. Check "Add Python to PATH"
echo 2. Check "Install for all users" (if you have admin rights)
echo.
pause

:: Run Python installer with recommended options
temp\python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

echo.
echo Installation completed. Verifying...
echo.

:: Refresh environment variables
call refreshenv >nul 2>&1

:: Check if Python is now available
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Python installation successful!
    python --version
    echo.
    echo You can now run setup_and_run.bat to set up the Care Point System.
) else (
    echo ❌ Python installation may have failed or PATH not updated.
    echo Please restart your computer and try again.
    echo If the problem persists, install Python manually from:
    echo https://www.python.org/downloads/
)

:: Clean up
if exist "temp\python-installer.exe" del "temp\python-installer.exe"
if exist "temp" rmdir temp

echo.
pause