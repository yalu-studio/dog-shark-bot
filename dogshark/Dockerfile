FROM python:latest

WORKDIR /

COPY . .

RUN python -m pip install --upgrade pip \
    && pip install -r requirements.txt

CMD python bot.py