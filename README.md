# Task API

A simple in-memory CRUD API built with **FastAPI**, as part of the FlyRank Backend Internship — Week 2, Assignment A1.

It manages a to-do list: you can create, read, update, and delete tasks. Data is stored only in memory, so it resets every time the server restarts.

## How to run it

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

Then open your browser to:
- `http://localhost:8000` — API info
- `http://localhost:8000/docs` — interactive Swagger UI

## Endpoints

| Method | Path             | Description                        |
|--------|------------------|-------------------------------------|
| GET    | /                | API info                            |
| GET    | /health          | Health check                        |
| GET    | /tasks           | List all tasks                      |
| GET    | /tasks/{task_id} | Get one task by id                  |
| POST   | /tasks           | Create a new task                   |
| PUT    | /tasks/{task_id} | Update an existing task's title/done |
| DELETE | /tasks/{task_id} | Delete a task                       |

## Example request

```bash
curl -i -X POST http://localhost:8000/tasks -H "Content-Type: application/json" -d "{\"title\":\"Buy milk\"}"
```

Response:
```
HTTP/1.1 201 Created
content-type: application/json

{"id":4,"title":"Buy milk","done":false}
```

## Status codes used

- `200` — successful read/update
- `201` — task created
- `204` — task deleted
- `400` — invalid input (e.g. empty title)
- `404` — task not found

## Swagger UI

<img width="1353" height="649" alt="Screenshot (595)" src="https://github.com/user-attachments/assets/e2ed7ddf-d5f9-4e82-b9f2-7a2045482a26" />
