from django.db import models
from django.contrib.auth.models import User
from users import UserFacebookStuff


# Create your models here.
class Pubkey(models.Model):
    key = models.TextField()
    user = models.ForeignKey(User)

    @classmethod
    def get_by_facebook_id(cls, fb_id):
        fb_user = UserFacebookStuff.get(facebook_id = fb_id)
        # TODO change when we want more keys per user
        return cls.objects.get(user = fb_user.user)
