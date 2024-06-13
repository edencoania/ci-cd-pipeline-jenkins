From python

RUN pip install gunicorn
RUN pip install flask
RUN pip install requests


COPY . /weather

WORKDIR /weather
CMD gunicorn -w 4 -b 0.0.0.0:1234 app:app


