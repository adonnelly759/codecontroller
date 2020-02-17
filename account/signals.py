from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Account

@receiver(post_save, sender=User)
def new_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(
            user = instance
        )