#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get -y update
    sudo apt-get -y upgrade
    sudo apt-get -y install nginx
fi 

sudo mkdir -p /data/web_static/releases//test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Check if the hbnb_static location block already exists before adding it
if ! grep -q "location \/hbnb_static {" /etc/nginx/sites-available/default; then
    sudo sed -i '/server_name _;/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
fi

sudo service nginx restart
