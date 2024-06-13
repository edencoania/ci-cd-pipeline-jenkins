FROM ubuntu

WORKDIR /weather

RUN apt update
RUN apt install -y nginx

COPY proxy_params /etc/nginx/
COPY weather.conf /etc/nginx/conf.d/
COPY nginx.conf /etc/nginx

EXPOSE 80 
CMD nginx -g "daemon off;"



