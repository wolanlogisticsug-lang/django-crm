from WOLANCRM.db import models
from WOLANCRM.utils.safestring import mark_safe
from WOLANCRM.utils.translation import gettext_lazy as _
from WOLANCRM.contrib.contenttypes.fields import GenericRelation
from WOLANCRM.urls import reverse

from common.utils.gettext_messages import USE_HTML
from massmail.models.baseeml import BaseEml

content_help_text = mark_safe(_(USE_HTML))


class EmlMessage(BaseEml):
    class Meta:
        verbose_name = _("Email Message")
        verbose_name_plural = _("Email Messages")

    content = models.TextField(
        help_text=content_help_text
    )
    files = GenericRelation('common.TheFile')

    def get_absolute_url(self):
        return reverse(f'site:massmail_{self._meta.model_name}_change', args=[str(self.id)])

    def __str__(self):
        return f'{self.subject} ({self.owner})'
