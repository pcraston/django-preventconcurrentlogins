from django.db import models
# FIXME: adapt to allow custom User model
from django.contrib.auth.models import User


class Visitor(models.Model):
    user = models.OneToOneField(User, null=False)
    session_key = models.CharField(null=False, max_length=40)