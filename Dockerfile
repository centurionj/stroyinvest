FROM python:3.10

WORKDIR /app

COPY /requirements.txt /app/requirements.txt
COPY ./stroyinvest/stroyinvest/celery.py /app/stroyinvest/stroyinvest/celery.py

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN apt-get update && \
    apt-get install -y nginx && \
    apt-get clean

COPY ./stroyinvest/ /app/
COPY /stroyinvest/deploy/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 8000

RUN chmod +x ./deploy/run.sh
CMD ["./deploy/run.sh"]