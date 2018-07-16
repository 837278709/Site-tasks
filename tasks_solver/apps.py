from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TaskAppConfig(AppConfig):
    name = 'tasks_solver'
    verbose_name = _('Celery Tasks')
