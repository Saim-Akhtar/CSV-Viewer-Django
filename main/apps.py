from django.apps import AppConfig

from .dataloader import load_data


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        # Load the data when the server starts
        load_data()
