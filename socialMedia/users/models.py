from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    followers = models.ManyToManyField(
        'self', related_name='following', symmetrical=False, blank=True)
    modified_on = models.DateTimeField(User, auto_now=True)

    def __str__(self):
        return self.user.username


def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile(user=instance)
        user_profile.save()

        user_profile.followers.add(instance.profile.id)
        user_profile.save()


post_save.connect(create_profile, sender=User)
