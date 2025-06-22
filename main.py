from fastapi import FastAPI, HTTPException
from schemas import TaskCreate, Task
from typing import List

app = FastAPI()

# Simulated database
tasks: List[Task] = []
task_id_counter = 1

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

@app.post("/tasks", response_model=Task)
def create_task(task: TaskCreate):
    global task_id_counter
    new_task = Task(id=task_id_counter, **task.dict())
    tasks.append(new_task)
    task_id_counter += 1
    return new_task

@app.delete("/tasks/{id}", response_model=Task)
def delete_task(id: int):
    global tasks
    for task in tasks:
        if task.id == id:
            tasks = [t for t in tasks if t.id != id]
            return task  # returning the deleted task
    raise HTTPException(status_code=404, detail="Task not found")
@app.put("/tasks/{id}", response_model=Task)
def mark_task_completed(id: int):
    global tasks
    for index, task in enumerate(tasks):
        if task.id == id:
            updated_task = Task(id=task.id, title=task.title, completed=True)
            tasks[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")
