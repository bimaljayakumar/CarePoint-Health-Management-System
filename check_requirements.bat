@echo off
echo ========================================
echo Care Point System - Requirements Check
echo ========================================
echo.

set "all_good=1"

:: Check Python installation
echo [1/4] Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ FAIL: Python is not installed or not in PATH
    echo    Please install Python 3.8+ from https://www.python.org/downloads/
    echo    Make sure to check "Add Python to PATH" during installation
    set "all_good=0"
) else (
    for /f "tokens=2" %%i in ('python --version 2^>^&1') do set python_version=%%i
    echo ✅ PASS: Python !python_version! is installed
)

:: Check pip installation
echo [2/4] Checking pip installation...
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ FAIL: pip is not available
    echo    pip should come with Python. Try reinstalling Python.
    set "all_good=0"
) else (
    echo ✅ PASS: pip is available
)

:: Check internet connectivity
echo [3/4] Checking internet connectivity...
ping -n 1 google.com >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ FAIL: No internet connection detected
    echo    Internet connection is required to download dependencies
    set "all_good=0"
) else (
    echo ✅ PASS: Internet connection is available
)

:: Check write permissions
echo [4/4] Checking write permissions...
echo test > test_write_permission.tmp 2>nul
if exist test_write_permission.tmp (
    del test_write_permission.tmp
    echo ✅ PASS: Write permissions are available
) else (
    echo ❌ FAIL: No write permissions in current directory
    echo    Try running as Administrator or choose a different location
    set "all_good=0"
)

echo.
echo ========================================
if "%all_good%"=="1" (
    echo ✅ ALL CHECKS PASSED!
    echo Your system is ready to run the Care Point System.
    echo You can now run setup_and_run.bat to install and start the application.
) else (
    echo ❌ SOME CHECKS FAILED!
    echo Please fix the issues above before running the setup.
)
echo ========================================
echo.

:: Additional system information
echo System Information:
echo - OS: %OS%
echo - Processor: %PROCESSOR_ARCHITECTURE%
echo - User: %USERNAME%
echo - Current Directory: %CD%
echo.

pause