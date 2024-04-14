Тестовое задание Avito

Структура:
task1.md - первое задание
png файлы (1 - 12) - скриншоты ошибок по первому заданию
test1.py - тест счетчика co2 (углекислого газа);
test2.py - счетчик объема воды;
test3.py - счетчик электроэнергии.
output - папка со скриншотами счетчиков (task2_1.png, task2_2.png, task2_3.png)

Инструкция тестирования счетчиков
1. Установка python 3.10;
2. Склонировать репозиторий git clone git@github.com/zm1518/avito_test_second.git;
3. Установка библиотеки playwright (команда - pip install pytest-playwright);
4. Установка версий для тестирования на playwright (команда playwright install)
5. Запуск тестов (команды  - pytest test1.py, pytest test2.py, pytest test3.py, pytest --headed test1.py, pytest --headed test2.py, pytest --headed test3.py)
