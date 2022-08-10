FROM python:3.8.5

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR /code

ENTRYPOINT python3 create_tables.py

CMD python3 start.py