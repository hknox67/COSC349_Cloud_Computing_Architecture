#!/bin/bash

sudo apt-get update
sudo apt-get upgrade

#vagrant upload ~/Desktop/Cosc349-main/assignment_one ~/ 

sudo apt-get install -y python3

#sudo python3 get-pip.py
#apt-get -y install python-pip
#python get-pip.py

sudo add-apt-repository universe

sudo apt-get install -y python3-pip
sudo apt-get install -y python3-dev libmysqlclient-dev build-essential
pip3 install mysql-connector-python
pip3 install mysqlclient

# this command installs the web framework for python         
pip3 install django
# The following commands install the additional web frameworks for python to create the admin website
pip3 install django-rest-framework

pip3 install djoser
# This command installs the image processors for magic the gathering cards within the website
pip3 install pillow

# Strpe is a payment processor, though it is not used directly by the wbesite it is needed for without there
# are a number of bugs which occour within the virtual machine.
pip3 install stripe
# This installs additional extensions used by the Django python web frameworks
pip3 install django_extensions

pip3 install django-cors-headers
# This command sets the defaul port number to run the admin webserer to the pot number specified by the vagrant file
#os.system("cd Desktop/Cosc349-main/assignment_one")
sudo python3 /vagrant/assignment_one/manage.py sqlflush

sudo python3 /vagrant/assignment_one/manage.py makemigrations

sudo python3 /vagrant/assignment_one/manage.py migrate

# sudo python3 /vagrant/assignment_one/manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')"
#os.system("cd Desktop/")
sudo python3 /vagrant/assignment_one/manage.py loaddata /vagrant/assignment_one/init_data.json
sudo python3 /vagrant/assignment_one/manage.py runserver 0.0.0.0:8700
# This command runs the manage.py file for the admin webserver

# python manage.py runserver

