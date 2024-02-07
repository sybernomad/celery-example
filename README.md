# celery-example

This repository provides a simple example demonstrating the usage of Celery, a distributed task queue library for Python.

## Overview

The example consists of two components:

### Alpha

The `alpha` component shows how to send a task to Celery for asynchronous execution. It uses Celery to send a task named `task_one`, which prints a provided detail string. The `alpha` component demonstrates how to:

- Initialize a Celery application
- Send a task for asynchronous execution
- Check the status of the task

To run the `alpha` component, use the following command:

```bash
poetry run python src/alpha/app.py
```

### Bravo

The `bravo` component demonstrates how to create a Celery worker to execute tasks asynchronously. It initializes a Celery application and sets up a worker to consume and execute tasks. The `bravo` component showcases how to:

- Initialize a Celery application
- Configure Celery to automatically discover tasks
- Start a Celery worker to process tasks

To run the `bravo` component, use the following command:

```bash
poetry run python src/bravo/app.py
```

## Usage

1. Start a Redis Docker container by running the following command:
```bash
docker run -it -d --rm -p 6379:6379 redis:latest
```
2. Start the `bravo` component by running the provided script.
3. Once the `bravo` worker is running, start the `alpha` component by running its script.
4. The `alpha` component will send a task to Celery, which will be processed by the `bravo` worker asynchronously.
5. Check the console output of both components to observe the execution of the task.

## Dependencies

This project uses Poetry for dependency management. Ensure that you have Poetry installed and run the following command to install the project dependencies:

```bash
poetry install
```
