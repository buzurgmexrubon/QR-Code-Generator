FROM python:3.9-slim

WORKDIR /app

COPY Pipfile Pipfile.lock requirements.txt ./

RUN pip install -r requirements.txt

COPY main.py ./

CMD [ "python", "main.py" ]
