@echo off
echo checking python installation...
echo.

:: python version
set python_version=3.11.5

::check system architecture
    if "%PROCESSOR_ARCHITECTURE%"=="x86" (
        echo 32-bit system detected.
    ) else (
        echo 64-bit system detected.
    )

:: if architecture is 32-bit, install python 3.11.4 x86
    if "%PROCESSOR_ARCHITECTURE%"=="x86" (
        echo 32-bit system detected.
        ::install python 3.11.4 x86
        powershell -Command "Invoke-WebRequest https://www.python.org/ftp/python/%python_version%/python-%python_version%-amd64.exe -OutFile python-%python_version%-amd64.exe"
        python-%python_version%-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
        where python >nul 2>nul
        if %errorlevel% neq 0 (
            echo python installation failed.
            echo.
            pause
            exit
        )
    ) else (
        ::install python 3.11.4 x64
        powershell -Command "Invoke-WebRequest https://www.python.org/ftp/python/%python_version%/python-%python_version%-amd64.exe -OutFile python-%python_version%-amd64.exe"
        python-%python_version%-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
        where python >nul 2>nul
        if %errorlevel% neq 0 (
            echo python installation failed.
            echo.
            pause
            exit
        )
    )

::check pip installation
where pip >nul 2>nul
if %errorlevel% neq 0 (
    echo pip is not installed.
    echo.
    pause
    exit
)

:: when python is installed delete the python installation file
del python-%python_version%-amd64.exe

:: if is not installed, install pip
powershell -Command "Invoke-WebRequest https://bootstrap.pypa.io/get-pip.py -OutFile get-pip.py"
python get-pip.py
del get-pip.py

::check pip version
pip --version

::if pip is not up to date, update pip
pip install --upgrade pip

:: install python packages
pip install -r requirements.txt

python main.py