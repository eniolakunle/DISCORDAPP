FROM python:bullseye

ENV PORT 5000

WORKDIR /discordapp

COPY requirements.txt /discordapp/requirements.txt

RUN pip install -r requirements.txt

COPY . /discordapp

CMD ["python3", "app.py"]