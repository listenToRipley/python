# Django Project

This document will go over specific for this project and not [Django general functionality notes](../../Notes/Django.md)

## Setup

Make sure you have your [pipenv running](../../Notes/Django.md/#setup).


This project contains the following applications:

### Shop

Allow end users to view course information.

#### Creation
Created by running `python manage.py startapp shop`

This created a [folder](./shop/) where this application will be stored, this is considered a package.

### API

Responsible for client requests via JSON formatting.

## Database

This project using sqlite database, the relationship is setup through [settings](./base/settings.py) and the [sqlite doc](./db.sqlite3).

To see the contents of this file, you will download and open [sqlite browser](https://sqlitebrowser.org/), find the path to the project and then "open database" and navigate to the db.sqlite3 document.

You can find more information about the [sqlite3 interface here](https://docs.python.org/3/library/sqlite3.html)

To create data in the database, migration will need to be applied. For new project  you may have seen the warning ```
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
``` 

[Review notes here for additional questions regarding migrations](../../Notes/Django.md/#migrations)