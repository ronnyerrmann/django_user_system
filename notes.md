
Create `user_system` project with app `iaido_users`:
```commandline
django-admin startproject user_system
python manage.py startapp iaido_users
python manage.py runserver 8800
```

After preparing the project, app, and model:
```commandline
python manage.py makemigrations iaido_users
python manage.py migrate
```

Once the database is created, add two users by first starting the shell:
```commandline
python manage.py shell
```
and then run
```
from iaido_users.models import Person
admin = Person(first_name="Andrea", last_name="Ghez", email="a_g@exists.not", phone="+1 234 567 8901", 
               dob="1965-06-16", username="adminU", is_staff=True, is_superuser=True)
admin.set_password("adminP")
admin.save()
user = Person(first_name="Donna", last_name="Strickland", email="d_s@exists.not", phone="+44 1234 567890", 
               dob="1959-05-27", username="userU")
user.set_password("userP")
user.save()
```