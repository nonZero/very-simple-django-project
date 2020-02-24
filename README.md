# This is a very simple django project.

* It was created with `django-admin startproject mydemo`.
* Dependencies are managed via `pipenv`.
* The settings are in [`mydemo.settings`](./mydemo/settings.py) 
* The only app we have is [`demoapp`](./demoapp/).  It has one model :-)
* Added `django-bootstrap4` and a simple bootstrap based template in [`base.html`](./demoapp/templates/base.html)

## Requirements

* Python 3.6+
* pipenv

## To setup in development:

    pipenv install
    pipenv run python manage.py migrate
    
## To run in development:

    pipenv run python manage.py runserver

