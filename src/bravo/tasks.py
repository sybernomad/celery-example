from app import app


@app.task
def task_one(detail: str):
    print(detail)
