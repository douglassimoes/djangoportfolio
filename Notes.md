# Django Portfolio App

Start a project
```
django-admin startproject portfolio .
```

Start an app
```
python manage.py startapp projects
```

Install the app inside settings.py of your project

Update the database to include and update your models
```
python manage.py makemigrations
python manage.py migrate
```

```
pip list --format=freeze > requirements.txt
```