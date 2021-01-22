FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y libgeos-dev 

WORKDIR /app
EXPOSE 80

RUN pip install -U pip setuptools wheel pipenv
COPY Pipfile* /app/
RUN pipenv lock --requirements > requirements.txt && pip install --no-cache-dir -r requirements.txt

COPY app /app/app

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]