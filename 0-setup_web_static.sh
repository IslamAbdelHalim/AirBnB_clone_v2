#!/usr/bin/env bash
# Prepare your web servers

# install nginx
sudo apt-get update
sudo apt-get -y install nginx

# create a data folder
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# create a html file

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# give the ownership and ownergroup
sudo chown -R ubuntu:ubuntu /data/

echo "server {
	listen 80;
	server_name _;
		root /var/www/html;

	index index.html index.htm;

	location /hbnb_static {
		alias /data/web_static/current;
	}
}" > /etc/nginx/sites-available/default

sudo service nginx restart
