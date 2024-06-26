from django.apps import AppConfig


class ShinaappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shinaApp'

    def ready(self):
        import shinaApp.signals