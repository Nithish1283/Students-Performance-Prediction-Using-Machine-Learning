@echo off
echo ==========================================================
echo   Students Performance Prediction - Local Server Launcher
echo ==========================================================
echo.
echo Activating virtual environment and starting Django server...
echo.
.venv\Scripts\python manage.py runserver
pause
