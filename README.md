# Portfolio Project based on Django

Here i am creating a portfolio project, which basically looks like a personal dashboard. Where you can keep a track of your ongoing projects, your activity and other things.

To build this project, i am using couple of things. like, Django framework for design, Python virtual environment to keep my active python directoy separate from root python directory and some HTML codes.

I will keep this place updated as i am progressing on this project.

Here i am going to explain, how to setup your personal environment for such projects.

# Step-1

First thing you need to do, is to create a personalized virtual environment for your project. But before than that, we got to create a directory in which you will be doing your work.

$ mkdir Project

$ cd Project

We are now inside the "Project" folder. Now, we will create a virtual environment.

install the virtual environment package if you don't have already

$ pip install virtualenv

Now, create your own virtual environment:

$ virtualenv Myenv

To get into your virtual environment, we need to activate Myenv:

$ source Myenv/bin/activate

Once you are inside your virtual environment, then whatever changes (installing/uninstalling packages) you do here, doesn't affect your python root profile.

To deactivate the virtual environment:

$ deactivate

For more details on Virtual Environment, follow below URL:
https://realpython.com/python-virtual-environments-a-primer/


# Step-2

We need to install the Django framework to build the profile. if you already have the existing django profile, then verify the version with this command:

$ python -m Django --version

if you don't have the latest Django version, then either install it or upgrade it.

$ pip install Django    >> for new installation

$ pip install Django --upgrade    >> To upgrade to some later release

Once the above setup is done, then we are all good to start with Django.

Some of the usefull Django commands:

$ django-admin startproject MyProject         >>> Used to create a new project folder

$ python manage.py runserver                  >>> To start the django server

$ python manage.py startapp blog              >>> To create an App

If some of the files are being migrated, then to create the migration use below command:

$ python manage.py makemigrations             >>> This one creates the migration

$ python manage.py migrate                    >>> This one performs the migration



# Step-3
I am using postgres for database management. You can download it from here https://postgresapp.com/downloads.html


P.S.: I will keep updating this place as i am progressing through this project.
