# Diplom_3

UI-автотесты для веб-приложения Stellar Burgers.

## Описание

Проект содержит автотесты, написанные с использованием паттерна Page Object.  
Тесты запускаются в двух браузерах: Google Chrome и Mozilla Firefox.

## Что тестируется

**Основная функциональность:**
- Переход по клику на «Конструктор»
- Переход по клику на раздел «Лента заказов»
- Всплывающее окно с деталями ингредиента
- Закрытие всплывающего окна кликом по крестику
- Увеличение счётчика ингредиента при добавлении

**Лента заказов:**
- Увеличение счётчика «Выполнено за всё время»
- Увеличение счётчика «Выполнено за сегодня»
- Появление номера заказа в разделе «В работе»

## Структура проекта

Diplom_3/
├── locators/      # Локаторы элементов
├── pages/         # Page Object классы
├── tests/         # Тесты
├── conftest.py    # Фикстуры
├── pytest.ini     # Конфигурация pytest
└── requirements.txt

## Установка

pip install -r requirements.txt

## Запуск тестов

pytest

Тесты запускаются в Chrome и Firefox автоматически.

## Allure-отчёт

allure generate allure_results -o allure_report --clean
allure open allure_report

## Стек

- Python 3.12
- pytest
- selenium
- allure-pytest
- webdriver-manager