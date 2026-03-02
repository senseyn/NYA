@echo off
chcp 65001 > nul
echo ЗАПУСК ЛОКАЛЬНОГО СЕРВЕРА

echo --создание виртуального окружения--
if not exist ".venv" (
    echo [INFO] Создание виртуального окружения...
    python -m venv .venv
) else (
    echo [INFO] Виртуальное окружение уже существует.
)

echo --активация venv--
call .venv\Scripts\activate

echo --установка библиотек--
call pip install -r requirements.txt

echo --запуск веб приложени--
python app.py

pause