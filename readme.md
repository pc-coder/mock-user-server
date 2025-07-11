# 🧪 Mock API Server for User Management

## 🚀 Features

- `GET /users` — List all users
- `GET /users/<id>` — Retrieve a single user
- `POST /users` — Create a new user
- `PUT /users/<id>` — Update a user
- `DELETE /users/<id>` — Delete a user

## 🛠️ Setup Instructions
docker build -t mock-users-api .
docker run -p 5000:5000 mock-users-api

## Local Development Setup
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
