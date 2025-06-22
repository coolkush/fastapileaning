from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    completed: bool = False

class Task(TaskCreate):
    id: int