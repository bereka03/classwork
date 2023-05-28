FROM python:3.8-slim-buster


RUN apt-get update
RUN apt-get install python3 python3-pip -y

ENV USER_ID=1000
ENV GROUP_ID=1000

RUN groupadd -g $GROUP_ID mygroup
RUN useradd -u $USER_ID -g $GROUP_ID myuser



RUN pip3 install flask
RUN pip3 install flask_sqlalchemy

RUN mkdir /app && mkdir /app/instance && chown myuser:mygroup /app/instance

USER myuser

COPY ./app.py /opt/
COPY ./templates /opt/templates

EXPOSE 5000

ENTRYPOINT ["python3", "/opt/app.py"]