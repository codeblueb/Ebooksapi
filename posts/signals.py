from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from users.models import CustomUser

@receover(post_save, sender=CustomUser, dispatch_uid="create_user_profile")
def save_profile(sender, instance, created, **kwargs):
    if created:
        profile = CustomUser(user=instance)
        profile.save()