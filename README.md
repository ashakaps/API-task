# API-task ML-эндпоинт для классификации вина

Сервис на FastAPI + Gradio, который по 13 химическим показателям партии вина определяет сорт винограда (`class_0`, `class_1`, `class_2`). Принимает запросы как через REST (JSON), так и через браузерный Gradio-интерфейс.

- **Live demo:** <https://194.67.121.156.nip.io/>
- **Swagger UI:** <https://194.67.121.156.nip.io/docs>
- **Health-check:** <https://194.67.121.156.nip.io/health>

## Что внутри

- обученная модель `DecisionTreeClassifier` на `sklearn.datasets.load_wine` с label noise 15% в train, подбор регуляризации (`max_depth=4`) через `GridSearchCV`. Регуляризация поднимает test accuracy с 0.76 (baseline) до 0.83 и сжимает train/test gap с 0.24 до 0.10
- `app/main.py` — FastAPI с lifespan-загрузкой модели + REST `/predict` + смонтированный Gradio на корневом пути `/`
- `tests/` — pytest-тесты на REST-эндпоинт и Gradio-роут
- `Dockerfile` + `.github/workflows/` — CI/CD, автодеплой на VPS через GHCR + SSH

## Архитектура

```mermaid
flowchart LR
    Browser[Browser] -->|GET /| Gradio[Gradio UI]
    Client[Programmatic client] -->|POST /predict| REST[FastAPI REST]
    Gradio -->|joblib.load| Model
    REST -->|joblib.load| Model
    Model[wine_model.pkl]
```

## Как запустить локально

```bash
conda create -n task-api python=3.11 -y
conda activate task-api
pip install -r requirements.txt

# запускаем сервис
uvicorn app.main:app --reload
```

Откройте `http://127.0.0.1:8000/` для Gradio, `http://127.0.0.1:8000/docs` для Swagger.

## Скриншот

![Gradio-интерфейс](screenshots/06_gradio_blocks_with_examples.jpg)

## Стек

Python 3.11 · FastAPI · Pydantic v2 · scikit-learn 1.6 · Gradio 5 · pytest · Docker · GitHub Actions · GHCR · nginx · Let's Encrypt
