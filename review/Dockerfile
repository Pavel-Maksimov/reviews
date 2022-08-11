FROM python:3.8.5

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x /script.sh

CMD ["/script.sh"]