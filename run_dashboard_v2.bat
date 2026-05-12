@echo off
REM This batch file starts a local HTTP server and opens dashboard_v2.html

echo Starting local server for Dashboard v2...
echo.

REM Get the directory of this batch file
cd /d "%~dp0"

REM Check if Python is available
python --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Python not found. Trying python3...
    python3 --version >nul 2>&1
    if %ERRORLEVEL% neq 0 (
        echo Error: Python is not installed or not in PATH
        echo Please install Python from https://www.python.org/downloads/
        pause
        exit /b 1
    )
    set PYTHON_CMD=python3
) else (
    set PYTHON_CMD=python
)

echo.
echo Starting HTTP Server on Port 8000...
echo Dashboard will open at: http://localhost:8000/dashboard_v2.html
echo.
echo Press Ctrl+C to stop the server
echo.

REM Start the browser
start http://localhost:8000/dashboard_v2.html
timeout /t 2 /nobreak

REM Start the HTTP server
%PYTHON_CMD% -m http.server 8000

pause
