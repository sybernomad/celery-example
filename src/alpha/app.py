import os
from time import sleep

from celery import Celery
from celery.result import AsyncResult


REDIS_URL = os.environ.get("REDIS_URL", "redis://0.0.0.0:6379")

app = Celery("alpha", broker=f"{REDIS_URL}/0", backend=f"{REDIS_URL}/1")


def get_status(task_id):
    result = AsyncResult(task_id, app=app)
    return {"task_id": task_id, "status": result.status}

def main():
    result = app.send_task(
        "tasks.task_one",
        args=["Hello, World!"],
    )

    sleep(1)
    print(get_status(result.id))


if __name__ == "__main__":
    main()
