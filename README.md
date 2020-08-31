# to_do_list

## Quick start
First download this project from [github](https://github.com/dt50/to_do_list) and bootstrap environment

```shell script
git clone https://github.com/dt50/to_do_list
cd to_do_list
poetry install
poetry shell
```
After that you need to migrate database and create superuser
```shell script
python3 manage.py migrate
python3 manage.py createsuperuser
```
And then you can start server
```shell script
python3 manage.py runserver
```

## URLS

/task/ - Create/Delete/Change users tasks
/user/ - Create user account or change info about him(login, password) 
/api/ - Api for integrate server with other program

## What's Included?
* [Django 3.0.7](https://www.djangoproject.com/)
* [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms)
* [django-rest-framework](https://www.django-rest-framework.org/)
* [djoser](https://github.com/sunscrapers/djoser)