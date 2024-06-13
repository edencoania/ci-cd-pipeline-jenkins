#!/bin/bash

sudo apt install nginx flask gunicorn

sleep(10)

sudo systemctl enable nginx
sleep(2)

sudo systemctl start nginx
sleep(5)

sudo cp weather.conf /etc/nginx/conf.d
sudo cp nginx.conf /etc/nginx/

pkill gunicorn&
pkill gunicorn&

sleep(5)

gunicorn -w 4 -b 127.0.0.1:1234 app:app&

sudo systemctl restart nginx
