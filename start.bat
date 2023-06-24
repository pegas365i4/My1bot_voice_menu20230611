@echo off

REM Замените <путь_к_вашему_виртуальному_окружению> на фактический путь к вашему виртуальному окружению

REM Активируем виртуальное окружение
call venv\Scripts\activate.bat

REM Запускаем main.py
python main.py

REM Деактивируем виртуальное окружение
call venv\Scripts\deactivate.bat

REM Завершаем выполнение скрипта
exit
