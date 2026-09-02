# FlyRank Backend Track — A4: Auth · Login & protect

Assignment #4 at FlyRank AI Internship. This is a task CRUD API — backed by PostgreSQL running in Docker — now secured with **Supabase Auth**. Users can sign up, log in, and log out, and specific routes are protected so they only respond to logged-in users with a valid access token.

## Tech stack

Python, FastAPI, PostgreSQL, SQLAlchemy, Supabase Auth, Pydantic, Docker, Docker Compose

## Prerequisites

You need Docker installed and running.

- Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) (free, Windows/Mac/Linux).
- Confirm it's running:
  ```bash
  docker --version
  docker ps
  ```

You also need a free [Supabase](https://supabase.com) account and project — no credit card required.

## Setup

1. Clone the repo and `cd` into the project folder.
2. Copy the environment template:
   ```bash
   cp .env.example .env
   ```
3. Create a free project at [supabase.com](https://supabase.com), then go to **Project Settings → API** and copy your **Project URL** and **anon key** into `.env`.
4. In your Supabase dashboard, go to **Authentication → Sign In / Providers → Email** and turn **OFF** "Confirm email" (so test signups can log in immediately without checking an inbox).
5. Fill in `.env`:
   ```dotenv
   DB_CONNECTION="postgresql://postgres:dev@localhost:5432/tasks"
   SUPABASE_URL="https://your-project-ref.supabase.co"
   SUPABASE_KEY="your-anon-key"
   PORT=8000
   ```

## How to run (one command)

```bash
docker compose up
```

The API is available at `http://localhost:8000`, with interactive docs at `http://localhost:8000/docs`.

To stop:
```bash
docker compose down
```

Task data persists across restarts via a Docker volume.

## Endpoint reference

| Route                         | Method | Auth required           | Purpose                         |
|-------------------------------|--------|--------------------------|----------------------------------|
| `/auth/signup`                | POST   | None                     | Create a new user account       |
| `/auth/login`                 | POST   | None                     | Authenticate & return a JWT     |
| `/auth/logout`                | POST   | Bearer token             | End the user's session          |
| `/public/info`                | GET    | None                     | Open, unauthenticated data      |
| `/protected/profile`          | GET    | Bearer token             | Read the logged-in user's data  |
| `/protected/dashboard`        | GET    | Bearer token             | Example second protected route  |
| `/tasks/create`               | POST   | None                     | Create a task                   |
| `/tasks/get_tasks`            | GET    | None                     | List all tasks                  |
| `/tasks/one_task/{id}`        | GET    | None                     | Get a single task               |
| `/tasks/update_task/{id}`     | PUT    | None                     | Update a task                   |
| `/tasks/delete_task/{id}`     | DELETE | None                     | Delete a task                   |

Protected routes expect an `Authorization: Bearer <access_token>` header, using the token returned from `/auth/login`.

## Example request/response

**Signup:**
```bash
curl -i -X POST http://localhost:8000/auth/signup \
  -H "Content-Type: application/json" \
  -d '{"email":"testuser@gmail.com","password":"password123"}'
```
→ `201 Created` with the new user object.

**Login:**
```bash
curl -i -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"testuser@gmail.com","password":"password123"}'
```
→ `200 OK`:
```json
{
  "status": "Login successful",
  "access_token": "eyJhbGciOi...",
  "refresh_token": "..."
}
```

**Accessing a protected route:**
```bash
curl -i http://localhost:8000/protected/profile \
  -H "Authorization: Bearer <access_token>"
```
→ `200 OK`:
```json
{
  "id": "6f269155-434d-4966-8780-22ae5721f5d9",
  "email": "testuser@gmail.com",
  "created_at": "2026-08-31T17:00:11.892558+00:00"
}
```

A missing, malformed, or invalid/expired token returns `401 Unauthorized` with a JSON error message.

## Swagger UI — bearer auth

`/docs` shows a padlock icon on every protected route. Click **Authorize**, paste an access token from `/auth/login` (no "Bearer" prefix needed — Swagger adds it), then use **Try it out** on any protected route directly from the browser.

_(Insert your Swagger screenshot here — Authorize dialog + a successful "Try it out" response on `/protected/profile`.)_

## Status codes

| Code | Meaning                                            |
|------|-----------------------------------------------------|
| 200  | Success (read / login)                              |
| 201  | Resource created (signup, task create)             |
| 204  | Success, no content (logout, task delete)          |
| 400  | Bad request — missing/invalid input                |
| 401  | Missing, malformed, or invalid/expired token        |
| 404  | Resource not found                                  |