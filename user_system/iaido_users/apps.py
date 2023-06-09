from django.apps import AppConfig


class IaidoUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'iaido_users'

    def ready(self):
        """Initialise users once the migration finished"""
        import iaido_users.signals
