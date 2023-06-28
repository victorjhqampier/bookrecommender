FROM python:3.10.11
WORKDIR /axapp

#RUN apt-get update && apt-get install -y --no-install-recommends gcc musl-dev unixodbc-dev unixodbc libpq-dev cron sudo
#RUN sudo service cron start

COPY . .
#RUN python -m pip install --upgrade pip
#[200~ENV FLASK_APP=myapp.py
#ENV FLASK_RUN_HOST=0.0.0.0
#ENV FLASK_RUN_PORT=5000
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"]
#CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0", "--workers=2"]
