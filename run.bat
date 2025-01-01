@echo off

REM Check if Venv exists
IF NOT EXIST ".venv" (
    echo Creating virtual environment...
    python -m venv .venv
    echo Installing dependencies...
    .venv\Scripts\pip install -r requirements.txt
)

REM Activate Venv
echo Activating virtual environment...
call .venv\Scripts\activate

REM Specify the full path to the Python executable
echo Running bot...
python .\src\main.py

REM Deactivate Venv
echo Deactivating virtual environment...
call .venv\Scripts\deactivate

REM Pause the terminal so you can see the output
pause


