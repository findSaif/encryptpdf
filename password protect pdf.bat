@ECHO OFF
pushd %~dp0
REM Run the python script to encrypt pdf files
python encrypt.py
popd
PAUSE