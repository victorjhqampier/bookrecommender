FROM python:3.10.11
WORKDIR /axapp

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0", "--reload", "app:app"]
#CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0", "--workers=2"]