FROM python:3.11-slim

WORKDIR /app

COPY app.py .

RUN pip install Flask

EXPOSE 5050

CMD ["python", "app.py"]
