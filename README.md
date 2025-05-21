# py-utils-collection

Набор Python-утилит: строгая проверка типов, парсинг Википедии и вычисление общего времени пересечения интервалов.
Написано на Python 3.11.

## Структура

- `task1` — Декоратор `@strict`, проверяющий типы аргументов
- `task2` — Скрипт для подсчета количества животных по буквам с Википедии
- `task3` — Функция для вычисления общего времени совместного присутствия на уроке

## Установка

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Запуск тестов

```bash
pytest
```
