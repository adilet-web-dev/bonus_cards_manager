from django.apps import AppConfig


class CardsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.cards"

    def ready(self):
        from . import jobs

        jobs.start_scheduler()
