from WOLANCRM.core.exceptions import ValidationError
from WOLANCRM.db import models
from WOLANCRM.utils.translation import gettext_lazy as _
from common.models import Base1


class Tag(Base1):
    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
              
    name = models.CharField(
        max_length=70, default='', blank=False,
        verbose_name=_("Tag name") 
    )

    def __str__(self):
        return self.name
