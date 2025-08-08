# Requirements

This project requires Docker Desktop installed and running.

# Install

Clone the repository

```bash
git clone git@github.com:falces/django.git
```

# Config

Clone the file `./docker/env.template` as `.docker/env` and edit its content:

```text
# DOCKER
COMPOSE_PROJECT_NAME=django
SERVICE_NAME=django

# DJANGO
DJANGO_SECRET_KEY=your_secret_key
DEBUG=True
DJANGO_LOGLEVEL=info
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

# DATABASE
# Use django.db.backends.sqlite3, django.db.backends.postgresql, django.db.backends.mysql, django.db.backends.oracle
# Others: https://docs.djangoproject.com/en/5.2/ref/databases/#third-party-notes
# DATABASE_ENGINE=postgresql_psycopg2
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME=dockerdjango
DATABASE_USERNAME=dbuser
DATABASE_PASSWORD=dbpassword
DATABASE_HOST=db
DATABASE_PORT=5432
```

# Run

With Docker Desktop running, execute:

```java
docker compose -f docker/compose.yaml up --build -d
```

# Migrations

Open a terminal into the Docker application container

```java
docker exec -it django_app /bin/sh
```

(If you've changed the application name, change them here)

And apply current migrations:

```java
python manage.py migrate
```

# Open

Open a web browser and navigate to:

```sh
http://localhost:8082/polls/
```

(If you've changed configurations, change them here)

The database is empty, create a poll question by making a POST request to:

```java
http://localhost:8082/polls/api/questions
```

With the body:

```json
{
    "id": 1,
    "question_text": "What's up?",
    "pub_date": "2025-08-08T00:00:00Z"
}
```