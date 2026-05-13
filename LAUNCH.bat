@echo off
REM ============================================================
REM DRG Payment Integrity Dashboard - Quick Launch Script
REM ============================================================
REM This batch file opens the dashboard in your default browser

setlocal enabledelayedexpansion

REM Get the directory where this script is located
set "script_dir=%~dp0"

REM Remove trailing backslash if present
if "!script_dir:~-1!"=="\" set "script_dir=!script_dir:~0,-1!"

REM Define the path to index.html
set "html_file=!script_dir!\index.html"

REM Check if index.html exists
if not exist "!html_file!" (
    echo Error: index.html not found in !script_dir!
    echo Please ensure index.html is in the same directory as this script.
    pause
    exit /b 1
)

REM Convert to full path for browser
set "full_path=file:///!html_file:\=/!"

REM Open in default browser
echo Launching DRG Payment Integrity Dashboard...
echo Opening: !full_path!
start !html_file!

REM Small delay to ensure browser window opens
timeout /t 2 /nobreak

exit /b 0
