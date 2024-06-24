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