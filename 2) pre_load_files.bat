@echo off
call _internal\setenv.bat

set /p path="Input File Path:"

"%PYTHON_EXECUTABLE%" "pre_process.py" "%path%"

pause