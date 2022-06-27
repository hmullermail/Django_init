# Getting Started With Django - Henrique Müller, 2022

### Creating a new Admin User, new application and new database table

Create an Admin User

```sh
python manage.py createsuperuser
```

Add a module (or application) to the project

```sh
django-admin startapp app_01
```

Add the new application to _settings.py_ file

Modify the _admin.py_ file to add it to the admin panel

Define new database tables in _models.py_ file and perform the migration procedure

```sh
python manage.py makemigrations app_01
python manage.py migrate
```
