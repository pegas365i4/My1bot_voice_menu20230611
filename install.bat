@echo off

REM Создаем виртуальное окружение
python -m venv venv

REM Активируем виртуальное окружение
call venv\Scripts\activate.bat

REM Устанавливаем библиотеку pyautogui
pip install -r requirements.txt

REM Деактивируем виртуальное окружение
call venv\Scripts\deactivate.bat

REM Завершаем выполнение скрипта
exit
