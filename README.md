# Farpost Category Classification

Тестовое задание - автоматическая классификация объявлений 
по категориям. Лестница из 3 моделей (TF-IDF -> CatBoost -> BERT) 
с полным error analysis.

## Структура

- `report.md` - финальный отчёт с результатами
- `ADR/` - Architecture Decision Records
- `01-05/` - ноутбуки по этапам
- `utils.py` - py methods

## Данные

Avito Demand Prediction Challenge (Kaggle)

## Запуск

1. `pip install -r requirements.txt`
2. Скачать `train.csv` от Avito Demand Prediction в `Data/`
3. Прогнать ноутбуки 01-05 по порядку
