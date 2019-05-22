# Deploy project on server
## Prepare common part

```bash
apt-get update
apt-get install git
mkdir /var/www
cd /var/www
git clone https://github.com/IlinValery/surdoportal-flask.git
git clone https://github.com/IlinValery/surdoportal-front.git

apt-get install -y python3 python3-pip nginx mysql-server libmysqlclient-dev supervisor unzip language-pack-ru
```

## Database settings
### Create database
```bash
mysql_secure_installation
mysql -p
```
```mysql
CREATE USER 'surdo_user'@'localhost' IDENTIFIED BY 'UserPass123)';
CREATE DATABASE surdoDB CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
GRANT ALL PRIVILEGES ON surdoDB.* To 'surdo_user'@'localhost';
```
### Fill database
```bash
cd /var/www/surdoportal-flask/docs
mysql -u surdo_user -p surdoDB < surdoDB.sql
```
## Flask settings
```bash
cd /var/www/surdoportal-flask/
pip3 install -r req.txt
pip3 install gunicorn
# If any problem, solve them here
# Check gunicorn project, for this add nginx file: 
nano /etc/nginx/sites-available/default
```
##### Nginx "default" file
```
server {
   listen 80 default_server;

  location / {
    proxy_pass http://localhost:5555;
  }
}
```
### Check gunicorn
```bash
gunicorn wsgi:application.server -b localhost:5555
#test nginx:
nginx -t
service nginx restart
```
#### Check here your flask app with browser next!

### Supervisor
```bash
nano /etc/supervisor/conf.d/gunicorn.conf
```
##### gunicorn.conf
```
[program:gunicorn]
command=/var/www/init.sh
autostart=true
autorestart=true
stderr_logfile=/var/log/gunicorn.err.log
stdout_logfile=/var/log/gunicorn.out.log
```
```bash
nano /var/www/init.sh
```
##### init.sh
```
#!/bin/sh
cd /var/www/surdoportal-flask
gunicorn wsgi:application.server -b localhost:5555
```
```bash
# Do not forget do chmod!!!
chmod +x /var/www/init.sh
```
#### Check supervisor
```bash
service supervisor start
supervisorctl reread
supervisorctl reload
update-rc.d supervisord defaults
systemctl enable supervisor
reboot
```

## React settings
### Prepare
```bash
cd /var/www/surdoportal-front/

curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
apt-get install -y nodejs
apt install npm
npm install -g create-react-app
npm i
```
### Build
```bash
npm run build
```
### Nginx
```bash
nano /etc/nginx/sites-available/default
```
##### Nginx "default" file
```
server {
   listen 80 default_server;
   root /var/www/surdoportal-front/build;
   index index.html;
   server_name surdoportal.neurability.ru;
   location / {
	try_files $uri /index.html;
   }
  location /api/ {
    proxy_pass http://localhost:5555/api/;
  }
}
```
#### Check nginx
```bash
nginx -t
service nginx restart
```
## Launch app by server IP