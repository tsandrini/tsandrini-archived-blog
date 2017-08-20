from django.apps import AppConfig
from core.admin.actions import register

class CoreConfig(AppConfig):
    name = 'core'
    verbose_name = "Core application"
    def ready(self):
        pass
