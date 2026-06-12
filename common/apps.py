from tendo.singleton import SingleInstanceException
from WOLANCRM.apps import AppConfig
from WOLANCRM.conf import settings
from WOLANCRM.utils.translation import gettext_lazy as _


class CommonConfig(AppConfig):
    name = 'common'
    verbose_name = _('Common')
    label = 'common'
    default_auto_field = 'WOLANCRM.db.models.AutoField'

    def ready(self):
        # Implicitly connect a signal handler
        from common.signals.handlers import user_creation_handler   # NOQA
        from common.utils.notif_email_sender import NotifEmailSender

        self.nes = NotifEmailSender()       # NOQA
        self.nes.start()
        if not settings.TESTING:
            from common.utils.reminders_sender import RemindersSender
            try:
                self.rs = RemindersSender()     # NOQA
                self.rs.start()
            except SingleInstanceException:
                pass
