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

Moving forward, this newly created folders will be called pack