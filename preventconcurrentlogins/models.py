from django.db import models
try:
    from django.contrib.auth import get_user_model
except ImportError:  # django < 1.5
    from django.contrib.auth.models import User
else:
    User = get_user_model()


class Visitor(models.Model):
    user = models.OneToOneField(User, null=False, related_name='visitor')
    session_key = models.CharField(null=False, max_length=40)