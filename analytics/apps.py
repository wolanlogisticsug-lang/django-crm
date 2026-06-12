from tendo.singleton import SingleInstanceException
from WOLANCRM.apps import AppConfig
from WOLANCRM.conf import settings
from WOLANCRM.utils.translation import gettext_lazy as _


class AnalyticsConfig(AppConfig):
    name = 'analytics'
    label = 'analytics'
    verbose_name = _('Analytics')
    default_auto_field = 'WOLANCRM.db.models.AutoField'
    
    def ready(self):
        if not settings.TESTING:
            from analytics.utils.monthly_snapshot_saving import MonthlySnapshotSaving
            try:
                self.mss = MonthlySnapshotSaving()      # NOQA
                self.mss.start()
            except SingleInstanceException:
                pass
