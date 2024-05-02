from django.db.backends.signals import connection_created
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from axes.signals import user_locked_out
from apps.core.exceptions import TooManyRequest


@receiver(user_locked_out)
def raise_permission_denied(*args, **kwargs):
    raise TooManyRequest()


@receiver(post_migrate)
def register_on_start(sender, **kwargs):
    print("AS",  kwargs.get('app_config'))