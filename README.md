# Farpost Category Classification

Тестовое задание - автоматическая классификация объявлений 
по категориям. Лестница из 3 моделей (TF-IDF -> CatBoost -> BERT) 
с полным error analysis.

## Структура

- `report.md` - финальный отчёт с результатами
- `docs/` - Architecture Decision Records (ADR)
- `notebooks/` - ноутбуки по этапам
- `utils.py` - вспомогательные функции|

## Данные

Avito Demand Prediction Challenge (Kaggle), 1.5M объявлений, 
47 категорий. Скачивание - см. notebooks/01_eda.ipynb.

## Запуск

1. `pip install -r requirements.txt`
2. Скачать `train.csv` от Avito Demand Prediction в `Data/`
3. Прогнать ноутбуки 01-05 по порядку
