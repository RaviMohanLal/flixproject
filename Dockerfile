# syntax-docker/dockerfile:1

FROM python:3.9.12

WORKDIR /raviflix-main

ADD . /raviflix-main

# COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
COPY . .

  #CMD ["python", "-m", "flask", "run"], "--host=0.0.0.0"]
CMD ["python", "main.py"]
#EXPOSE 5000