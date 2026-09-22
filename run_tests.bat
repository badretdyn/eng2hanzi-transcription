@echo off
@REM  chcp 65001 >nul
@REM  set PYTHONIOENCODING=utf-8
@REM  set PYTHONUTF8=1

@REM  cd /d "%~dp0"

python -m tests.test_model

pause