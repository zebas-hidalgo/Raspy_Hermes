FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt pyproject.toml /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
RUN pip install --no-cache-dir -e .

CMD ["python", "-m", "raspy_hermes.main"]
