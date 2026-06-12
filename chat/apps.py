from WOLANCRM.apps import AppConfig
from WOLANCRM.utils.translation import gettext_lazy as _


class ChatConfig(AppConfig):
    name = 'chat'
    label = 'chat'
    verbose_name = _('Chat')
    default_auto_field = 'WOLANCRM.db.models.AutoField'
