from iaido_users.models import Person
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def create_initial_user(sender, **kwargs):
    if not Person.objects.exists():
        admin = Person(
            first_name="Andrea", last_name="Ghez", email="a_g@exists.not", phone="+1 234 567 8901", dob="1965-06-16",
            username="adminU", is_staff=True, is_superuser=True
        )
        admin.set_password("adminP")    # to hash the password
        admin.save()
        user = Person(
            first_name="Donna", last_name="Strickland", email="d_s@exists.not", phone="+44 1234 567890",
            dob="1959-05-27", username="userU"
        )
        user.set_password("userP")
        user.save()
