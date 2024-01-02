FROM python:3.10

WORKDIR /app

RUN apt-get update && \
    apt-get install -y nginx && \
    apt-get clean

COPY /requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY ./stroyinvest/ /app/

EXPOSE 8000

RUN chmod +x ./deploy/run.sh
CMD ["./deploy/run.sh"]