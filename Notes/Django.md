# Django

[Official docs](https://www.djangoproject.com/)

For notes about the specifics of the [example project review this README](../Examples/django_proj/README.md)

Django is a MVC system by which you can create and manage your content; however; instead of this being MVC in django, this is known as MTV.

Django is made up of applications and middleware included in the original installation. You can see all that are included in this structure by review [settings](../Examples/django_proj/base/settings.py). This applications and middleware are starting point and they can be modified or new ones added.

## MCV -> MTV

The contempt between MCV to MTV stays the same, but the terminology used makes a small shift.

### Model

M - [Model](https://docs.djangoproject.com/en/5.0/topics/db/models/), (Model -> Model) which is the interface for interaction with data. This is a level of abstraction that allows use to modify that data stored in the database. As a result, this is considered a security improvement.

### Template

T - [Template](https://docs.djangoproject.com/en/5.0/topics/templates/) (View -> Template), visible interface aka the the presentation. You can also think of these as the different pages that are generated on different devices. From the user's perspective though, they should have no preservable knowledge of the View nor Model. If can provide instructions of your applications for where to find the different templates in the [settings](../Examples/django_proj/base/settings.py)

### View

V - [View](https://docs.djangoproject.com/en/5.0/topics/http/urls/) (Controller -> View), the logic the dictates the interactions of the interface (templates) with the data (model). The view does not work with the database directly, but goes through the model. 

## Setup

This project is using [pip env](./VirtualEnv.md/#create-venv-inside-project), once installed then used `pipenv install Django==4.2.2`, install the folder, then run `pipenv shell` and create the starting folder with `django-admin startproject base .`

This command will crease manage.py and a base folder. Base is a type of package that is available locally.

The manage.py file s the "django's command-line utility for administrative tasks".

### Start Server

Inside of your `pipenv shell` 

Then run `python manage.py runserver`

### Adding Applications

Creating application/packages within your Django project allows you to create an easy way to organize the functionality of your project. To create a new one, run `python manage.py startapp app_name`, you should see a new folder created in your project. 

Moving forward, this newly created folders will be called packages since that is what they are.

Keep in mind, you will not be able to view this package contents until it has been added to base's urls file.

#### New Package Items

What is included in this newly created packages and what do they do? 

*Folder*

##### Migrations

Contains an __init__ file.

The items hav been automatically enabled are the `INSTALLED_APPS` in your [settings](../Examples/django_proj/base/settings.py). This items will need to have data in the database.

While you pipenv shell is running, go to a new terminal window inside your project and run `python manage.py migrate`, this will apply all items lists in your variable above.

##### Files

- __init__

Empty file.

- admin

Where models are registered to perform administrative tasks.

- apps

A class that contains attributes of the package, it will be the package name plus "Config"

- models

This is where your [models](./Django.md/#model) that will interact with your database will be stored. 

- tests

Where your test cases will be stored.

- views 

This is your controllers that will connect your [view with models.](./Django.md/#view), this is where all our logic for sending and receiving requests between the models and the client templates.

### Enable Package

You will need to add your views and [create a url paths specific to the package.](../Examples/django_proj/shop/urls.py)

It's important to note that when you are importing your views, import all and then specific the view you want to use for a specific path to prevent collisions.

This we need to add this package urls to the base urls by using the includes function, [example](../Examples/django_proj/base/urls.py)

## General Info

WSGI - Web Server Gateway Interface, this application is responsible for serving the rest of our application to the web and different end clients, (ex. ngix or apache). This is the default option. 

ASGI - Asynchronous Server Gateway Interface, this is the alternative to WSGI and is included in your Django package, but is turned off by default.

### Database

The database relationship is outlined in the [settings document](../Examples/django_proj/base/settings.py)

### Best Practices

The "DEBUG" variable is base settings should be changed to false once the application is push to production.

#### Base

Since application/packages will be stored on the same level, we need a base of operations for the general requested/starting information for a Django project, base should be considered as your global variable storage for your project. 

Using the name base makes this easy to identify that folder. 
