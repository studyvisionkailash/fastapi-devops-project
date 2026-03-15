from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI DevOps Demo Running 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}

tasks = []

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: dict):
    tasks.append(task)
    return {"message": "Task added"}
