from django.db import models
from django.contrib.auth.models import User


class Visitor(models.Model):
    user = models.OneToOneField(User, null=False)
    session_key = models.CharField(null=False, max_length=40)