FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1
ENV DB_USER=redhat 
ENV DB_PASSWORD=redhat123 
ENV DB_DATABASE=persistentdb 
ENV DB_HOST=10.8.0.64  
ENV DB_NAME=postgresql-persistent 
ENV DB_PORT=5432
USER root
RUN apt update && apt install -y gcc nano libpq-dev python-dev && apt install -y nginx
RUN pip install --upgrade pip
RUN mkdir /code
RUN ls -ltr
RUN chmod -R 777 /code
RUN ls -ltr
WORKDIR /code
# add all the requirements for the applicaiton in the requirements.txt file.
COPY requirement.txt /code/requirement.txt
RUN pip install -r requirement.txt
COPY nginx/nginx.conf /etc/nginx/
COPY nginx/sites-enabled.conf /etc/nginx/conf.d/
COPY . /code/
#Expose the port
EXPOSE 8002
# add necessary permissions
RUN chgrp -R 0 /var/log/nginx/ /var/run/ /usr/share/nginx/ /code/nginx/ /var/lib/nginx/
RUN chmod -R g+rwx /var/log/nginx/ /var/run/ /usr/share/nginx/ /code/nginx/ /var/lib/nginx/
# Uncomment below line if db file not uploadded
RUN cd /code && python3 manage.py makemigrations && python3 manage.py migrate
# trying to run postgress
#RUN chmod -R 777 /code/db.sqlite3
USER 1001
CMD nginx && gunicorn --env DJANGO_SETTINGS_MODULE=soar_dispatch_pro.settings --workers 4 --bind 127.0.0.1:8001 soar_dispatch_pro.wsgi:application --timeout 120
