from django.apps import AppConfig


class IntendanceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Intendance'

    def ready(self):
        import Intendance.signals