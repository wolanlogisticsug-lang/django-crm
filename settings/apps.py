from WOLANCRM.apps import AppConfig
from WOLANCRM.utils.translation import gettext_lazy as _


class SettingsConfig(AppConfig):
    name = 'settings'
    label = 'settings'
    verbose_name = _('Settings')
    default_auto_field = 'WOLANCRM.db.models.AutoField'
