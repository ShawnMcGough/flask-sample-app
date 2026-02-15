# Copilot Instructions for Flask Sample App

## Architecture

- **Flask application factory style (simple variant):** The `Flask` app instance is created in `app/__init__.py` and routes are imported at module level via `from app import routes`. No blueprints—all routes live in `app/routes.py`.
- **In-memory data store:** Items are stored in a module-level `items = []` list in `app/routes.py`. There is no database; data resets on restart and is shared across requests within a process.
- **Entry point:** `run.py` imports and runs the app (`app.run()`).

## Key Conventions

### Route patterns (`app/routes.py`)
- Routes return plain strings or `dict` (auto-serialized to JSON by Flask).
- Error responses return a JSON dict with an `"error"` key and the appropriate HTTP status code as a second return value: `return {'error': 'Item not found'}, 404`.
- Success mutations return a JSON `"message"` key: `return {'message': 'Item added successfully'}, 201`.
- Items are accessed by list index (`item_id` = positional index in `items`).

### Testing (`tests/test_app.py`)
- Framework: **pytest** (run with `pytest` from the project root).
- Uses a `client` fixture that sets `app.testing = True` and yields `app.test_client()`.
- Tests validate both `status_code` and the JSON/body content of each response.
- Each route has at least a happy-path test and, where applicable, an error-case test (e.g., 404 for missing items).
- Note: `tests/__init__.py` imports `flask_testing.TestCase` but tests themselves use plain pytest style—follow the pytest pattern.

## Developer Workflow

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app (http://localhost:5000)
python run.py

# Run all tests
pytest
```

## Adding a New Endpoint

1. Add the route function in `app/routes.py`, following existing patterns (dict returns, error key for failures, message key for successes).
2. Add corresponding tests in `tests/test_app.py` using the `client` fixture—cover both success and error paths.
3. Feature specs may live in `specs/` as markdown files (see `specs/delete-feature.md` for an example).

## Dependencies

Pinned in `requirements.txt`: Flask 2.3.3, pytest 8.3.4. No ORM, no database driver—keep it minimal.
