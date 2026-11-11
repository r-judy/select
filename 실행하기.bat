@echo off
chcp 65001 >nul
title 발표자 뽑기 프로그램

echo ========================================================
echo         🎯 발표자 뽑기 프로그램 실행기
echo ========================================================
echo.
echo 1. 웹 화면으로 실행 (추천: 애니메이션, 효과음, 더블클릭 실행)
echo 2. 파이썬 콘솔 프로그램 실행 (main.py)
echo 3. 원본 파이썬 코드 실행 (original_picker.py)
echo.
set /p choice="원하시는 모드를 선택해주세요 (1, 2, 3): "

if "%choice%"=="1" (
    echo.
    echo 웹 브라우저에서 실행합니다...
    start index.html
    exit /b
)

if "%choice%"=="2" (
    echo.
    echo 파이썬 콘솔 프로그램을 실행합니다...
    python main.py
    if errorlevel 1 (
        echo.
        echo [안내] 파이썬이 설치되어 있지 않거나 경로 설정이 필요합니다.
        echo index.html 을 더블 클릭하면 브라우저에서 바로 사용하실 수 있습니다!
        pause
    )
    exit /b
)

if "%choice%"=="3" (
    echo.
    echo 원본 파이썬 프로그램을 실행합니다...
    python original_picker.py
    if errorlevel 1 (
        echo.
        echo [안내] 파이썬이 설치되어 있지 않거나 경로 설정이 필요합니다.
        pause
    )
    exit /b
)

echo 잘못된 입력입니다. index.html을 직접 더블클릭하여 실행하실 수도 있습니다.
pause

