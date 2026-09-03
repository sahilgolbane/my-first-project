# Task Manager API

A backend REST API for managing tasks with user accounts and authentication. Built with FastAPI and PostgreSQL, containerized with Docker, and deployed live to the cloud.

**🌍 Live Demo:** https://task-manager-sahil.onrender.com/docs

*(The interactive API docs let you try every endpoint directly in the browser. First load may take ~30 seconds as the free server wakes up.)*

---

## What it does

This API lets users sign up, log in, and manage their own personal to-do tasks. Each task belongs to a specific user, and protected routes ensure users can only access their own data using secure token-based authentication.

## Features

- **User authentication** — signup and login with securely hashed passwords (bcrypt) and JWT token-based sessions
- **Protected routes** — endpoints that require a valid token to access
- **Full CRUD for tasks** — create, read, update, and delete tasks
- **User–task relationships** — each task is linked to a user via a foreign key; users can fetch only their own tasks
- **Data validation** — incoming request data is validated with Pydantic before it reaches the database
- **Cloud database** — connected to a managed PostgreSQL instance
- **Containerized & deployed** — packaged with Docker and running live on Render

## Tech Stack

| Area | Technology |
|---|---|
| Language | Python |
| Framework | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Validation | Pydantic |
| Auth | JWT (python-jose) + bcrypt (passlib) |
| Containerization | Docker |
| Deployment | Render |

## API Endpoints

**Authentication**
- `POST /signup` — create a new account
- `POST /login` — log in and receive a JWT token
- `GET /me` — get the current logged-in user (protected)

**Users**
- `GET /users` — list all users
- `GET /users/{id}` — get a single user
- `GET /users/{id}/tasks` — get all tasks belonging to a user

**Tasks**
- `GET /tasks` — list all tasks
- `GET /tasks/{id}` — get a single task
- `POST /tasks` — create a task
- `PUT /tasks/{id}` — update a task
- `DELETE /tasks/{id}` — delete a task

## Running Locally

```bash
# clone the repo
git clone https://github.com/sahilgolbane/my-first-project.git
cd my-first-project/task-manager

# install dependencies
pip install -r requirements.txt

# run the server
uvicorn main:app --reload
```

Then open `http://127.0.0.1:8000/docs` in your browser.

## Running with Docker

```bash
docker build -t task-manager .
docker run -p 8000:8000 task-manager
```

---

## About This Project

I built this project to teach myself production backend development end to end — from writing the API and designing the database schema, to adding authentication, containerizing with Docker, and deploying it live to the cloud with a managed database. Every part was written and debugged by hand to genuinely understand how a real backend fits together.
