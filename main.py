from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class TaskCreate(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    title: str | None = None
    done : bool |None = None


tasks = [{'id': 1, 'title': 'meet a friend', 'done' : True},
        {"id": 2, "title": "Read a book", "done": True},
        {"id": 3, "title": "Clean the house", "done": False},]

@app.get("/", summary="API info", description="Returns the name, version and available endpoints of this API.")
def read_root():
    return {'name' : 'Task API',
            'version' : '1.0',
            'endpoints': ['/tasks']}



@app.get('/health', summary="Health check", description="Returns ok if the server is alive. Used to check the server is running.")
def health_check():
    return {'status': 'ok'}


@app.get('/tasks', summary="List all tasks", description="Returns the full list of tasks currently stored in memory.")
def get_tasks():
    return tasks

@app.get('/tasks/{task_id}', summary="Get one task", description="Returns a single task by its id. Returns 404 if the task does not exist.")
def get_task(task_id : int):
    for task in tasks:
        if task['id'] == task_id:
            return task

    raise HTTPException(status_code = 404, detail=f"Task {task_id} not found" )

@app.post("/tasks", status_code=201, summary="Create a task", description="Creates a new task with the given title. The task starts as not done.")
def create_task(task: TaskCreate):
    if not task.title.strip():
        raise HTTPException(status_code=400, detail="Title cannot be empty")

    new_id = max((t["id"] for t in tasks), default=0) + 1
    new_task = {"id": new_id, "title": task.title, "done": False}
    tasks.append(new_task)
    return new_task

@app.put('/tasks/{task_id}', summary="Update a task", description="Updates the title and/or done status of an existing task. Returns 404 if the task does not exist.")
def update_task(task_id: int, update: TaskUpdate):
    for task in tasks:
        if task['id'] == task_id:
            if update.title is not None:
                if not update.title.strip():
                    raise HTTPException(status_code = 400, detail = 'Title can not be empty')
                task['title'] = update.title
            if update.done is not None:
                task['done'] = update.done
            return task
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

@app.delete('/tasks/{task_id}', status_code =204, summary="Delete a task", description="Deletes a task by its id. Returns 404 if the task does not exist.")
def delete_task(task_id: int):
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            return
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
