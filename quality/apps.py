from WOLANCRM.apps import AppConfig
from WOLANCRM.utils.translation import gettext_lazy as _


class QualityConfig(AppConfig):
    default_auto_field = 'WOLANCRM.db.models.AutoField'
    name = 'quality'
    verbose_name = _('Transaction quality')
    label = 'quality'
