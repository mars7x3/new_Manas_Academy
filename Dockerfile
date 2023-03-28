FROM python:3.8

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN apt-get update
RUN apt-get install -y libgdal-dev
RUN export CPLUS_INCLUDE_PATH=/usr/include/gdal
RUN export C_INCLUDE_PATH=/usr/include/gdal

COPY ./rex.txt /usr/src/rex.txt
RUN pip install -r /usr/src/rex.txt

COPY . /usr/src/app
RUN ["chmod", "+x", "/usr/src/app/entrypoint.sh"]
