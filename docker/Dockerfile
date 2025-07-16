FROM python:3.12.3-alpine3.20

WORKDIR /src

COPY ./docker/.env .

# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1
# Avoid Python to create __pycache__ files in project
ENV PYTHONPYCACHEPREFIX=~/.cache/cpython/

RUN pip install --upgrade pip

COPY ./requirements.txt  .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./manage.py .

EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]