FROM python:3.12

ENV PYTHONDOMTWRITEBYTECODE 1
ENV PYTHONUNBUFFEERD 1

WORKDIR /app

COPY requirements.txt . 

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "filemanagementsys.wsgi", "--bind", "0.0.0.0:8000", "--workers", "4"]