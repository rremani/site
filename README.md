# hypothizer-lab

## How to setup the project

1. clone the project in you workspace `git clone https://github.com/vipin14119/hypothizer-lab.git`
2. Make sure you have pip installed , we are using python 2.7 in this project so run this to get latest stable pip `sudo apt-get install python-pip`
3. Now if you want to work in a seperate virtual environment then run this `sudo pip install virtualenv`
4. Run `sudo apt-get install python-dev` for python dev tools
5. Run `sudo apt-get install libjpeg-dev libjpeg8-dev` for supporting images handling in django
6. Now create a virtualenv by `virtualenv virtual`, it will create a virutal environment named `virtual`
7. activate your environment by `source virtual/bin/activate`
8. now move into directory of project `cd hypothizer-lab/server`
9. Run pip install -r requirements.txt
10. All project requirements should be installed properly by doing this

## How to Fire up the server

1. `cd hypothizer-lab/server`
2. apply migrations of project `python manage.py makemigrations`
3. commit migrations `python manage.py migrate`
4. It should create a sqlite3.db named document in project folder , thats you database (Dont edit or open this)
5. Run `python manage.py runserver` now your server should be running on your loopback address (Check terminal if its showing any errors)
6. Go to browser and hit enter to the adress `127.0.0.1:8000`
7. That's it for firing up server

