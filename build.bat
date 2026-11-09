@echo off
title VideoTranscriber EXE Builder

cd /d "%~dp0"

echo ========================================
echo       VideoTranscriber EXE Builder
echo ========================================

echo.
echo Installing requirements...

py -m pip install -r requirements.txt

if errorlevel 1 (
    echo ERROR: Requirements installation failed.
    pause
    exit /b 1
)

echo.
echo Installing PyInstaller...

py -m pip install pyinstaller

if errorlevel 1 (
    echo ERROR: PyInstaller installation failed.
    pause
    exit /b 1
)

echo.
echo Building GUI executable...

py -m PyInstaller --noconfirm --clean --onefile --windowed --name VideoTranscriber app.py

if errorlevel 1 (
    echo ERROR: EXE build failed.
    pause
    exit /b 1
)

echo.
echo ========================================
echo BUILD COMPLETED SUCCESSFULLY
echo ========================================

echo.
echo EXE location:
echo %~dp0dist\VideoTranscriber.exe

pause