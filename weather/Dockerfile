From python as flask_weather


COPY . /weather

WORKDIR /weather

#RUN apt update
#RUN apt install -y nginx

RUN pip install flask
RUN pip install requests
RUN pip install boto3

FROM flask_weather

WORKDIR /weather

RUN apt update
RUN apt install -y nginx

COPY weather.conf /etc/nginx/conf.d/
COPY nginx.conf /etc/nginx
RUN pip install gunicorn

EXPOSE 80 
CMD nginx -g "daemon off;" & gunicorn -w 4 -b 0.0.0.0:1234 app:app


