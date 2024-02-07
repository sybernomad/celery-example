import os

from celery import Celery


REDIS_URL = os.environ.get("REDIS_URL", "redis://0.0.0.0:6379")

app = Celery("bravo", broker=f"{REDIS_URL}/0", backend=f"{REDIS_URL}/1")
app.autodiscover_tasks(["tasks"])
app.conf.update(task_track_started=True)


def main():
    app.worker_main(["worker", "--loglevel=info", "-c", "1"])


if __name__ == "__main__":
    main()
