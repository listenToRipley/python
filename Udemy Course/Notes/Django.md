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

Make sure any additional package that you need to install use `pipenv install PACKAGE_NAME` and if required include version.

### Start Server

Inside of your `pipenv shell` 

Then run `python manage.py runserver`

### Adding Applications

Creating application/packages within your Django project allows you to create an easy way to organize the functionality of your project. To create a new one, run `python manage.py startapp app_name`, you should see a new folder created in your project. 

Moving forward, this newly created folders will be called packages since that is what they are.

Keep in mind, you will not be able to view this package contents until it has been added to base's urls file.

#### New Package Items

What is included in this newly created packages and what do they do? And should be done once they are created?

*Folder*

##### Migrations

Contains an __init__ file.

The items hav been automatically enabled are the `INSTALLED_APPS` in your [settings](../Examples/django_proj/base/settings.py). This items will need to have data in the database.

While you pipenv shell is running, go to a new terminal window inside your project and run `python manage.py migrate`, this will apply all items lists in your variable above. Now if you refresh your database you should see all data fields created for this db.

After you have complete the [models setup](#model), then you would run `python manage.py makemigrations` and django will take take of the migration requirements. You should see in the terminal that specific migrations were created and added to the migrations folder. This file will help format requests that will be sent to the database.

After your changes have been applied, restart your server and you will need to apply the newly created content to be migrated by running `python manage.py migrate`. After this has been applied, you should now see the content in the database.

Don't modify the file name that are automatically generated.

##### Files

###### __init__

Empty file.

###### admin

Where models are registered to perform administrative tasks.

######  apps

A class that contains attributes of the package, it will be the package name plus "Config"

######  models

This is where your models that will interact with your database will be stored.

These models exist as a representation of a singular record in the database. It is best practice to not use plurals when naming these elements.

These elements are stored as an extended classes of `models.Model`. 

Think of the class name a the table name and the attributes as the columns for that table. Since the attributes will be the columns, the values are going to be their storage values, the type of data we will be retaining and any additional parameters associated with those value, (how long it can be, if it has a default etc...) Some of these models values will require additional imports to provide the correct functionality.

To create a relationship between two models, you can use `models.ForeignKey(ClassName)`

You may want to use `on_delete=models.CASCADE`, which means if the class name is ever removed, then so will all associated courses.

For items to be appear in the database that has been provided in the model, verify that the configuration has included in your [apps.py](../Examples/django_proj/shop/apps.py) for the associated application, you will need to add that configuration class name to your the INSTALLED_APP section of the [setting.py file](../Examples/django_proj/base/settings.py). The format for the direction to this will be the `folder.file.class`. After these changes have been made, make sure you restart your server.

[Review classes for additional questions](./Classes.md)

*__Modifying models__*

If you need to make changes to the content of your database, make alterations to your models file and then you will need to run [migrations again](#migrations)

###### tests

Where your test cases will be stored.

###### Permissions

In order to allow access to do something to your models best practice state that you should authenticate (who you are) and authorize (what you can do once you get there). You need to [import that functionality](../Examples/django_proj/api/models.py) to your application and assign to a variable that will be referenced for API calls.

###### views 

This is your controllers that will connect your [view with models.](#view), this is where all our logic for sending and receiving requests between the models and the client templates.

You will create your views as http responses, but in order to make management of your views easier, you will need to create a [templates folder.](#templates)

Once your [templates](#templates) have been added, you will use django shortcuts to render your content by passing in that template, [see example here](../Examples/django_proj/shop/views.py). 

The direct path to your template does not have to be specified since it should exist inside the same parent folder. The reason django knows this is since it is specified in the [setting](../Examples/django_proj/base/settings.py) under `TEMPLATES` since the `'APP_DIRS': True`. This would be a good place to check if you are having issues with your content not appearing.

To pass content to your template, use will pass it as a dictionary.

### Enable Package

You will need to add your views and [create a url paths specific to the package.](../Examples/django_proj/shop/urls.py)

It's important to note that when you are importing your views, import all and then specific the view you want to use for a specific path to prevent collisions.

This we need to add this package urls to the base urls by using the includes function, [example](../Examples/django_proj/base/urls.py)

Make sure in each of your url application docs you include `app_name='application_name'`. This will allow django to find different applications use within your project and make routing easier. Best practice states that the name of your application that you use should make the base url provided for that applications in [here](../Examples/django_proj/base/urls.py)

#### Nested Routes

When you create additional paths on an application, then will be considered nested as their base url will be used before any specified paths.

To add theses, within the [urls doc under the url patterns](../Examples/django_proj/shop/urls.py) you add that different views that are associated with the templates you want to use.

If you are using a given variable to return a given template, then you would pass in the value type and variable name to that the path: `<type:variable_name>` and then specify the view. This will allow you to call the database with that value as the parameter.

You can create relative links by adding the value to the front `path/<type:variable_name>`. 

To create relative paths in the template, you would add the matching value to your href. The sames goes for creating absolute paths. Neither of these methods are considered best practice as it will require changes to all locations where the path is used instead of changes to a single variable.

The best way to pass your paths is first you add a name variable to the url patterns and the in your template is to use your urls paths `url "app_name:route_name" variable.id`

#### API Routes

You can [reuse the name path of multiple items.](../Examples/django_proj/base/urls.py) This means that if you share the path, all items that base route. This is usually use in the case of an api raw request that will return results of that call.

The base route used in the starting point, but the model created should provide the desired output from the given call. The route dependencies, the arguments provided after the base, those will be determined by the content provided in your [model](../Examples/django_proj/api/models.py). You should see the table contents returned as well as variables provided inside of your Meta class. This section will also determine what html methods you are able to perform.

Depending on the package you used, that will determine the format type, but you may need to review your extensions to change the display of that format.

Since our example project is using [tastypie](https://django-tastypie.readthedocs.io/en/latest/), the results will be in JSON format.

##### Versions 

Use versions for your API to provide allow for different API calls to be use or discontinues, this would be done in your [routing](../Examples/django_proj/base/urls.py). Each version will have to be registered for that given resource.

Since you have to use `api.register(resource_name)`, then under your `urlpatterns`, you would no longer have to use a specified patterns like `path('api/', include(resource_name.urls))`, you just have all the api's grouped together under that register.

This does mean that the version control does have to be included in the route though before the arguments.

If you need information about what could be provided in this call, you can use the path just the version.

For the keyword schema, this will provide details on what could be returned and they types of the contents of the call,(via url), it would look something like this: `BASEURL/api/version/table/schema`.

##### HTML Calls

With the [API model](../Examples/django_proj/api/models.py) class, you must specify the types of methods that be allowed under the `allow_method`. If the type of HTML call is not outlined there, you will receive an error what this is attempted.

To restrict access or customize authentication, (such as being `GET` always accessible), you can create an [customized process](../Examples/django_proj/api/authentication.py)

###### Keys

If you create an API key for your calls within the admin site, that content will be required moving forward to all API calls. The key would look something like: `Authorization: ApiKey username:apiKeyHere123`

###### DELETE and POST

The [API model](../Examples/django_proj/api/models.py) must contain variable that [assign the authentication and authorization.](#permissions), one those variable have been assigned to the class, then you should get a 200 code that provides details on what was one. If you receive a 400 code, make sure to validate your keys, (via the admin on panel) and review your model to make sure that import and variable have been correctly assigned.


## General Info

WSGI - Web Server Gateway Interface, this application is responsible for serving the rest of our application to the web and different end clients, (ex. ngix or apache). This is the default option. 

ASGI - Asynchronous Server Gateway Interface, this is the alternative to WSGI and is included in your Django package, but is turned off by default.

If you want to run anything through the python interpreter, you can use `python manage.py shell` to launch it.

### Database

The database relationship is outlined in the [settings document](../Examples/django_proj/base/settings.py), but in order to add content to your database from your application, you will need to set up [models](#models) and include [migrations](#migrations) so all elements can interact.

#### Creating Data

##### via Shell

Running the python interpreter inside of the document, you would import the [models](#models) you want to use and create a new class, it would look something like this:

```python
from shop.models import Category

new_category = Category(title='Programming')
new_category.save()

category = Category.objects.get(pk=1)

category.course_set.create(title="Complete Python Guide", price=0.99, students_qty=100, reviews_qty=30)

category.course_set.all()

[course.title for course in category.course_set.all()]
```

The method save is what will push your content to be added to the database.

If you wanted to see all data the currently exists in the terminal, you can run `ClassName.objects.all()`. Make use the class has been imported like Category above. This will return the number of entries, not details of the content. You should be able to access the content by using dot notation. 

To find a specific entry, you can use `ClassName.objects.get(pk=#)`. "pk" being your Primary Key. You could then assign it to a variable and access the content via dot notation. You don't have to use "pk", you could use any column header for that table and even use dot notation to return different content that would match. 

You could filter by running `ClassName.objects.filter(pk=#)`. Filter does offer some arguments such as `columnName__containing="*"`

##### via Admin

You will need to [import models in the admin file](../Examples/django_proj/shop/admin.py) through the files included in your models file. Once your have completed the registration, then you should be able to refresh your application page and see the items listed on the admin page. You should be able to add, edit and delete all items that exist in the database through this interface.

To change the name/titles displayed in the admin site, you need to provide a method to your [model class](../Examples/django_proj/shop/models.py) that will return the associated name/title you want returned inside of the object quantity.

#### Modifying tables

If you need to make changes to the structure of you database, those changes should be applied to your [model class](../Examples/django_proj/shop/models.py), then run `python manage.py makemigrations`. After you will need to restart the server and reapply `python manage.py migrate` to see those changes in the database. If default data is note provided, those need fields will be blank and need to be populated.

### Templates

Inside your application, you will create a [templates folder](../Examples/django_proj/templates/), where you will store your content for display. This will need to be linked back to your [views](#views) in order for the content to be assessed in your application. 

If you have data that needs to be based, it will be done in your view via dictionaries. 

To use the passed data, you will [use django template formatting.](https://docs.djangoproject.com/en/5.0/ref/templates/language/).

For a better structure and easier access, it is best that the templates folder exist at the root of your project. In order to django to still access your different applications to use these templates, make sure that the [settings file](../Examples/django_proj/base/settings.py) under `TEMPLATES`, the variable `DIR` include the base path and the path to the associated file; e.g. `'DIR': [BASE_DIR / 'templates_folder_name']`

It also will create a better structure if each applications templates have their own sub folders to create better organization and easier navigation. This means that in your views you need to be more specific about the location of your html documents within the template structure.

#### Styling

You can use a number of styling libraries with django, this example [uses bootstrap.](https://getbootstrap.com/docs/5.3/getting-started/introduction/). To access this bootstrap library on these templates, you will add the CDN link for CSS to the head section, [example](../Examples/django_proj/templates/base.html).

In order to keep your templates concise, create a single point of entry, called, [base](../Examples/django_proj/templates/base.html) and then [extend each piece of dependent content](../Examples/django_proj/templates/courses.html). You need to indict each template used on the base by name.

### Best Practices

- The "DEBUG" variable is base settings should be changed to false once the application is push to production.

- Don't modify models once you have data in your database.

- Don't recreate models that already exist, just import them from the related application and reuse them; [e.g. shop in api](../Examples/django_proj/api/models.py)

- Your API routes should be protected.

#### Base

Since application/packages will be stored on the same level, we need a base of operations for the general requested/starting information for a Django project, base should be considered as your global variable storage for your project. 

Using the name base makes this easy to identify that folder. 

### Resources

To organize use API services,the two most popular options are [django rest framework](https://www.django-rest-framework.org/) and [Tastypie.](https://django-tastypie.readthedocs.io/en/latest/). Django rest framework is very powerful and was considered overkill for the example project here so tastypie was used instead.