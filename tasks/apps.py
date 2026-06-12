from WOLANCRM.apps import AppConfig
from WOLANCRM.utils.translation import gettext_lazy as _


class TasksConfig(AppConfig):
    name = 'tasks'
    label = 'tasks'
    verbose_name = _('Tasks')
    default_auto_field = 'WOLANCRM.db.models.AutoField'
