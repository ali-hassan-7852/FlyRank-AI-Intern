# FlyRank Backend Track — A3: Containerize your stack

Assignment #3 at FlyRank AI Internship. This app is a task CRUD API — previously backed by in-memory storage (A1) and SQLite (A2) — now running against a real **PostgreSQL** database inside **Docker**, with the entire stack (API + database) started using a single command via **Docker Compose**.

## Tech stack

Python, FastAPI, PostgreSQL, SQLAlchemy, Pydantic, Docker, Docker Compose

## Prerequisites

You need Docker installed and running — that's the only manual setup required.

- Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) (free for personal use, Windows/Mac/Linux).
- After installing, make sure the Docker Desktop app is open and running before continuing.
- Confirm it works:
  ```bash
  docker --version
  docker ps
  ```
  `docker ps` should return an empty table (not an error).

No local Python install, no local Postgres install, and no manual database setup are needed — Docker handles all of that.

## How to run (one command)

No manual database setup, no local Postgres install. Everything runs in containers.

```bash
git clone <your-repo-url>
cd <project-folder>
cp .env.example .env
docker compose up
```

The API will be available at `http://localhost:8000`, with interactive docs at `http://localhost:8000/docs`.

To stop everything:
```bash
docker compose down
```

Your data persists across restarts (`docker compose down` then `docker compose up` again) because it's stored in a Docker volume, not inside the container itself.

## Environment variables

Create a `.env` file in the project root (a git-ignored file — never commit real credentials). Use `.env.example` as a template:

```dotenv
DB_CONNECTION="postgresql://postgres:dev@localhost:5432/tasks"
```

> Note: when running via `docker compose up`, the app connects to the database using the service name `db` instead of `localhost` — this is already configured inside `compose.yaml` and requires no action from you.

## Endpoint table

| CRUD operation | HTTP Method | Path                | Meaning                  |
|-----------------|-------------|----------------------|---------------------------|
| Create          | POST        | `/create_task`       | Create a new task        |
| Read (all)      | GET         | `/all_task`          | List all tasks           |
| Update          | PUT         | `/update_task/{id}`  | Update a task by id      |
| Delete          | DELETE      | `/delete_task/{id}`  | Delete a task by id      |

## Example request/response

```bash
curl -i http://localhost:8000/all_task
```

```
HTTP/1.1 200 OK
content-type: application/json

{
  "status": "Tasks retrieved successfully",
  "data": [
    { "id": 1, "name": "Buy groceries", "info": "Milk, eggs, bread", "is_complete": false },
    { "id": 2, "name": "Write report", "info": "Q3 summary for team", "is_complete": false },
    { "id": 3, "name": "Call dentist", "info": "Reschedule appointment", "is_complete": true }
  ]
}
```

## Database screenshot

_(Add a screenshot here showing your data inside Postgres — e.g. via `docker exec -it taskdb psql -U postgres -d tasks` running `\dt` and `SELECT * FROM "User_Data";`, or a GUI tool like DBeaver/pgAdmin.)_