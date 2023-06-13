from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.core.management import call_command

class IaidoUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'iaido_users'

    def ready(self):
        """ Make migrations for the in-memory database, as the database is removed every time the process restarts
        (every time the database connection is closed)
        - However, with that the migrations are still not applied
        call_command('migrate',
                     app_label='iaido_users',
                     verbosity=1,
                     interactive=False,
                     )"""

        # Initialise the basic users once the migration finished
        import iaido_users.signals
