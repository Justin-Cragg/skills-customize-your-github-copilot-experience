# 🧩 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small RESTful API using the FastAPI framework. The API should expose CRUD endpoints for a simple resource, validate input, and run locally with `uvicorn`.

## 📝 Tasks

### 🛠️ Core API

#### Description
Create a FastAPI application that manages a collection of "items" (an in-memory store is fine). Implement endpoints to create, read, update, and delete items.

#### Requirements

- Implement the following endpoints:
  - GET /items — list all items
  - GET /items/{item_id} — get a single item
  - POST /items — create a new item (validate payload)
  - PUT /items/{item_id} — update an existing item
  - DELETE /items/{item_id} — remove an item
- Use Pydantic models for request validation and response schemas.
- Return appropriate HTTP status codes (201 for create, 404 for not found, etc.).
- Keep the main app in `starter-code/main.py` and ensure it runs with `uvicorn starter-code.main:app --reload`.

### ✨ Optional Enhancements

- Add query parameters for filtering or pagination on `GET /items`.
- Add simple authentication (API key via header) for write operations.
- Persist data to a JSON file so the data survives restarts.

## Example Requests

Create item (JSON):

POST /items
{
  "name": "Notebook",
  "description": "200 pages",
  "price": 3.5
}

Response: 201 Created with the created item JSON.

## Notes for Submission

- Ensure `starter-code/main.py` starts a FastAPI `app` object and includes example routes.
- Include `requirements.txt` with FastAPI and Uvicorn pinned.
- To run locally:

```bash
python3 -m pip install -r requirements.txt
python3 -m uvicorn starter-code.main:app --reload
```

If you add extra files (data files, modules), list them and add short usage notes here.
