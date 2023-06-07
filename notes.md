
Create `user_system` project with app `iaido_users`:
```commandline
django-admin startproject user_system
python manage.py startapp iaido_users
python manage.py runserver 8800
```

After preparing the project and app:
```commandline
python manage.py migrate
```

After creating the model:
```commandline
python manage.py makemigrations iaido_users
```