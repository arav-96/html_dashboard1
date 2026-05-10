@echo off
cd /d "%~dp0"
start "DRG Dashboard Server" /min cmd /c "python -m http.server 8001"
timeout /t 2 /nobreak >nul
start "" "http://localhost:8001/dashboard.html"
