FROM python:3.10

WORKDIR /app

RUN apt-get update && \
    apt-get install -y nginx && \
    apt-get clean

COPY /requirements.txt /app/requirements.txt
COPY ./stroyinvest/stroyinvest/celery.py /app/stroyinvest/stroyinvest/celery.py

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

RUN mkdir -p /app/media && \
    chown -R 1000:1000 /app/media

COPY ./stroyinvest/ /app/
COPY /stroyinvest/deploy/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 8000

RUN chmod +x ./deploy/run.sh
CMD ["./deploy/run.sh"]