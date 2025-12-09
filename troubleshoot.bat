@echo off
echo ========================================
echo Care Point System - Troubleshooting Tool
echo ========================================
echo.

:menu
echo Select an option:
echo 1. Reset virtual environment
echo 2. Reinstall dependencies
echo 3. Reset database
echo 4. Check system requirements
echo 5. Fix common permission issues
echo 6. Clean temporary files
echo 7. View error logs
echo 8. Exit
echo.
set /p choice="Enter your choice (1-8): "

if "%choice%"=="1" goto reset_venv
if "%choice%"=="2" goto reinstall_deps
if "%choice%"=="3" goto reset_db
if "%choice%"=="4" goto check_reqs
if "%choice%"=="5" goto fix_permissions
if "%choice%"=="6" goto clean_temp
if "%choice%"=="7" goto view_logs
if "%choice%"=="8" goto exit
goto menu

:reset_venv
echo.
echo Resetting virtual environment...
if exist "venv" (
    echo Removing existing virtual environment...
    rmdir /s /q venv
)
echo Creating new virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo ERROR: Failed to create virtual environment!
    pause
    goto menu
)
echo Virtual environment reset successfully.
pause
goto menu

:reinstall_deps
echo.
echo Reinstalling dependencies...
if not exist "venv" (
    echo Virtual environment not found. Creating one...
    python -m venv venv
)
call venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip uninstall -y -r requirements.txt
pip install -r requirements.txt
echo Dependencies reinstalled successfully.
pause
goto menu

:reset_db
echo.
echo Resetting database...
if exist "db.sqlite3" (
    echo Backing up existing database...
    copy db.sqlite3 db.sqlite3.backup
    del db.sqlite3
)
if exist "venv" (
    call venv\Scripts\activate.bat
    python manage.py migrate
    echo Database reset successfully.
) else (
    echo Virtual environment not found. Please run setup first.
)
pause
goto menu

:check_reqs
echo.
call check_requirements.bat
pause
goto menu

:fix_permissions
echo.
echo Fixing common permission issues...
echo Attempting to fix file permissions...
icacls . /grant %USERNAME%:(OI)(CI)F /T >nul 2>&1
if %errorlevel% equ 0 (
    echo Permissions fixed successfully.
) else (
    echo Could not fix permissions automatically.
    echo Try running this script as Administrator.
)
pause
goto menu

:clean_temp
echo.
echo Cleaning temporary files...
if exist "__pycache__" rmdir /s /q __pycache__
for /d /r . %%d in (__pycache__) do @if exist "%%d" rmdir /s /q "%%d"
if exist "*.pyc" del /s *.pyc
if exist ".pytest_cache" rmdir /s /q .pytest_cache
echo Temporary files cleaned.
pause
goto menu

:view_logs
echo.
echo Recent error information:
echo ========================
echo.
echo Python version:
python --version 2>&1
echo.
echo Pip version:
pip --version 2>&1
echo.
echo Virtual environment status:
if exist "venv" (
    echo ✅ Virtual environment exists
) else (
    echo ❌ Virtual environment missing
)
echo.
echo Database status:
if exist "db.sqlite3" (
    echo ✅ Database file exists
) else (
    echo ❌ Database file missing
)
echo.
echo Environment file status:
if exist ".env" (
    echo ✅ .env file exists
) else (
    echo ❌ .env file missing
)
echo.
pause
goto menu

:exit
echo.
echo Troubleshooting complete.
echo If issues persist, please check the SETUP_INSTRUCTIONS.md file.
pause
exit /b 0