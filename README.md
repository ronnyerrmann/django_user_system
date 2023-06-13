### To run the API locally (all commands run in django_user_system/user_system)
After pulling the project:
```commandline
python manage.py makemigrations iaido_users
python manage.py migrate
```

Once the migration has finished, two users will be created automatically. Their login details are:

| User name | Password |
| ---       | ---      |
| userU     | userP    |
| adminU    | adminP   |

The server can then be started (in my case on local port 8800)
```commandline
python manage.py runserver 8800
```

Tests are run by
```commandline
python manage.py test
```

### Without pulling this project
Create `user_system` project with app `iaido_users`:
```commandline
django-admin startproject user_system
python manage.py startapp iaido_users
```
Afterwards continue with the steps above, assuming  the project, app, and model are still prepared and the users are still being added
