from django.db import models
from django.contrib.auth.models import User
from open_facebook import OpenFacebook

class UserFacebookStuff(models.Model):

    user = models.ForeignKey(User)

    facebook_id = models.TextField()
    access_token = models.TextField()

    def get_graph_api(self):
        """Return Facebook Graph API object initialized with user's token"""
        return OpenFacebook(self.token)

