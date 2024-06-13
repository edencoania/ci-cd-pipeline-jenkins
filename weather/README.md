hey - this is guide to install eden weather app on server.

first - make sure you don't have gunicorn prosses that work, 
and you need to keep it working.

copy all the files inside the director

inside the file - weather.conf - write the ip of your machine.
---------------------------

RUN - the following commands. 

cd ./weather

sudo chmod +s /path-to startall.sh #give sudo privelged to script. 

source start_all.sh 			# or bash start_all.sh


it will install nginx, flask, gunicorn - place the nginx configuration files in the rigth positions
and it will restart nginx server and start gunicorn with 5 instances of app.py
that is the weather

eden coania

