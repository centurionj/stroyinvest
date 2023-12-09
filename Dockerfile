FROM python:3.10

WORKDIR /app

COPY /requirements.txt /app/requirements.txt
#COPY ./stroyinvest/stroyinvest/celery.py /app/stroyinvest/stroyinvest/celery.py

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y nginx && apt-get clean

COPY ./stroyinvest/ /app/
COPY /stroyinvest/nginx/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 8000

CMD sh -c "python /app/manage.py migrate && \
          python /app/manage.py collectstatic --noinput && \
          gunicorn stroyinvest.wsgi:application --bind 0.0.0.0:8000 & \
          celery -A stroyinvest worker -l info & \
          nginx -g 'daemon off;'"