FROM python:3.9-alpine

ARG SYS_ENV
ENV SYS_ENV ${SYS_ENV}
WORKDIR /home/geo-user
COPY . /home/geo-user/
RUN pip install -r /home/geo-user/src/requirements.txt
EXPOSE 8080
CMD ["gunicorn", "--config", "/home/geo-user/src/gunicorn_conf.py", "src.echo_server:app"]