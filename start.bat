@echo off
title mkproject - Setup
echo ==============================================
echo   mkproject CLI Setup
echo ==============================================
echo.

REM Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Python was not found in PATH.
    echo Please install Python from https://www.python.org/downloads/
    echo and make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)

echo [1/3] Python found. Checking version...
python --version

echo.
echo [2/3] Installing mkproject in editable mode...
pip install -e .
if %errorlevel% neq 0 (
    echo [ERROR] Installation failed. See the error above.
    pause
    exit /b 1
)

echo.
echo [3/3] Fixing PATH if needed...
if exist fix-path.ps1 (
    powershell -ExecutionPolicy Bypass -File fix-path.ps1
) else (
    echo [WARNING] fix-path.ps1 not found — skipping PATH fix.
)

echo.
echo ==============================================
echo   Setup complete!
echo   Close this window and open a NEW terminal,
echo   then run: mkproject
echo ==============================================
pause