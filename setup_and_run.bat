@echo off
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing required packages...
pip install moviepy

echo Running Python script...
python convert_gif_to_mp4.py

echo Done.
pause
