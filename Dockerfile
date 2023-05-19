FROM python:3.10.11
WORKDIR /axapp

RUN apt-get update && apt-get install -y --no-install-recommends gcc musl-dev unixodbc-dev unixodbc libpq-dev cron sudo
RUN sudo service cron start

COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0", "--workers=2"]
