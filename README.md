# VideoTranscriber

A Windows desktop video transcription application built with Python, Tkinter, and Faster-Whisper.

## Tested Environment

* Operating System: Windows 11
* Python: 3.14.8 (64-bit / AMD64)
* Faster-Whisper: 1.2.1
* PyAV (`av`): 18.1.0
* FFmpeg: 9.0.2
* PyInstaller: 6.22.3
* Whisper model: `base`
* Device: CPU
* Compute type: `int8`

## What the application does

1. Selects a video file.
2. Transcribes the video using Faster-Whisper on the CPU.
3. Creates timestamps in `HH:MM:SS` format.
4. Lets the user choose where to save the `.txt` transcription file.

## Source Code Setup

### 1\. Install Python

Install Python 3.14.8 (64-bit) on Windows.

Verify:

```powershell
python --version
```

Expected:

```text
Python 3.14.8
```

### 2\. Create a virtual environment

Open Command Prompt or PowerShell in the project folder:

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\\Scripts\\activate
```

### 3\. Install Python dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4\. Install FFmpeg

Install FFmpeg for Windows and make sure the `ffmpeg` command is available in PATH.

Verify:

```powershell
ffmpeg -version
```

The development environment used for this project was:

```text
FFmpeg 9.0.2
```

### 5\. Run the source code

```powershell
python app.py
```

## Building the Windows EXE

Install PyInstaller:

```powershell
python -m pip install pyinstaller==6.22.3
```

Build a single-file GUI executable:

```powershell
pyinstaller --onefile --noconsole --name VideoTranscriber app.py
```

The resulting executable will be:

```text
dist\\VideoTranscriber.exe
```

## Important Notes

* The `venv` folder should not be copied to another developer's computer. It is machine-specific.
* `Test.mp4` is only a test file and is not required by the application.
* The packaged `VideoTranscriber.exe` is intended for users who do not have Python installed.
* The first run of Faster-Whisper may download the selected Whisper model if it is not already available locally.
* The current application uses the `base` Whisper model with CPU `int8` computation.

