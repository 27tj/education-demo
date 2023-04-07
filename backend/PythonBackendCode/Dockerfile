#Get the Python 3.10 Image
FROM python:3.10

#Install Python dependency
RUN pip install flask-marshmallow

RUN pip install Flask-SQLAlchemy

RUN pip install uuid

#Change the directory to /usr/app/src
WORKDIR /usr/app/src

#Copy Python Code into docker Image
COPY main.py ./

COPY ./HTTPResovers ./

