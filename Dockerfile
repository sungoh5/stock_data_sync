FROM python:3.8-slim-buster

WORKDIR /stock-data-sync

COPY .version setup.py start.py ./
COPY app ./app

RUN pip install .

CMD [ "python", "start.py"]