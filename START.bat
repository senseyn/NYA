@echo off
chcp 65001 > nul
echo ЗАПУСК ЛОКАЛЬНОГО СЕРВЕРА

echo --активация venv--
call .venv\Scripts\activate

echo --запуск приложени--
python app.py

pause