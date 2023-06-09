
Create `user_system` project with app `iaido_users`:
```commandline
django-admin startproject user_system
python manage.py startapp iaido_users
```

After preparing the project, app, and model:
```commandline
python manage.py makemigrations iaido_users
python manage.py migrate
```

Once the migration has finished, two users will be created. Their login details are:

| User name | Password |
| ---       | ---      |
| userU     | userP    |
| adminU    | adminP   |

The server can then be started (in my case on local port 8800)
```commandline
python manage.py runserver 8800
```