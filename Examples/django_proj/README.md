# Django Project

This document will go over specific for this project and not [Django general functionality notes](../../Notes/Django.md)

## Setup

Make sure you have your [pipenv running](../../Notes/Django.md/#setup).

### Tech

Database will be [sqlite3 interface here](https://docs.python.org/3/library/sqlite3.html)

Template CSS display will be [bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/). We will install via the CDN links, (only CSS) which will be added to the head section, [example](./templates/base.html)

If you are using VSCode, you can install [Django Templates](https://marketplace.visualstudio.com/items?itemName=bibhasdn.django-html) to make template work easier.

For API, we will use [Tastypie.](https://django-tastypie.readthedocs.io/en/latest/)

To make requests easier to read, you can use [JSON Formatter](https://chromewebstore.google.com/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa?pli=1)

For API calls use [Postman](https://www.postman.com/)

### Applications

This project contains the following applications:

#### Shop

Allow end users to view course information.

##### Creation
Created by running `python manage.py startapp shop`

This created a [folder](./shop/) where this application will be stored, this is considered a package.

##### Model

Inside the shop, we will have categories and courses. The relationship will be one to many, the one being the categories and the courses being the many.

Review [models for general questions](../../Notes/Django.md/#models)

The categories to courses is a one to many relationship.

#### API

Responsible for client requests via JSON formatting. This will allow access to database, courses and categories, which we will consider "resources".

The tool used for this is [Tastypie](https://django-tastypie.readthedocs.io/en/latest/), specifically version 0.14.5.

## Database

This project using sqlite database, the relationship is setup through [settings](./base/settings.py) and the [sqlite doc](./db.sqlite3).

To see the contents of this file, you will download and open [sqlite browser](https://sqlitebrowser.org/), find the path to the project and then "open database" and navigate to the db.sqlite3 document.

You can find more information about the [sqlite3 interface here](https://docs.python.org/3/library/sqlite3.html)

To create data in the database, migration will need to be applied. For new project  you may have seen the warning 

```
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
``` 

[Review notes here for additional questions regarding migrations](../../Notes/Django.md/#migrations)

Kee