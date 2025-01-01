FROM python:3.10.12-slim

WORKDIR /app

COPY . .

RUN python3 -m pip install -r requirements.txt

ENV FLASK_APP=app.__init__:create_app

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
