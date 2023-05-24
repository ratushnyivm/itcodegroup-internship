FROM python:3.11.2

COPY req.txt /tmp

RUN pip install -r /tmp/req.txt

COPY . /opt/app

WORKDIR /opt/app

CMD ["python", "manage.py", "runserver", "0:8000"]
