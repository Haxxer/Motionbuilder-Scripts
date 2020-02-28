@echo off
SET mypath=%~dp0
python %mypath:~0,-1%/progressbar.py
ping 127.0.0.1 -n 2 > nul