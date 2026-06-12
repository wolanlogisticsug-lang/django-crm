from WOLANCRM.contrib.auth.models import Group
from WOLANCRM.db.models.signals import post_save
from WOLANCRM.dispatch import receiver

from common.models import UserProfile
from common.utils.helpers import USER_MODEL


@receiver(post_save, sender=USER_MODEL)
def user_creation_handler(sender, instance, created, **kwargs):
    if created:
        try:
            co_workers = Group.objects.get(name='co-workers')
        except Group.DoesNotExist:
            co_workers = None
        if co_workers:
            instance.groups.add(co_workers)
        UserProfile.objects.get_or_create(user=instance)
