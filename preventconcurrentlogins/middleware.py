try:
    from django.contrib.auth import get_user_model
except ImportError:  # django < 1.5
    from django.contrib.auth.models import User
else:
    User = get_user_model()
from django.contrib.sessions.models import Session
from django.conf import settings

from models import Visitor


class PreventConcurrentLoginsMiddleware(object):
    """
    Django middleware that prevents multiple concurrent logins..
    Adapted from http://stackoverflow.com/a/1814797 and https://gist.github.com/peterdemin/5829440
    """

    def process_request(self, request):
        if isinstance(request.user, User):
            key_from_cookie = request.session.session_key
            if hasattr(request.user, 'visitor'):
                session_key_in_visitor_db = request.user.visitor.session_key
                if session_key_in_visitor_db != key_from_cookie:
                    Session.objects.filter(session_key=session_key_in_visitor_db).delete()
                    request.user.visitor.session_key = key_from_cookie
                    request.user.visitor.save()
                    # if using cache or cached_db session, also clear cache
                    if settings.SESSION_ENGINE in ('django.contrib.sessions.backends.cached_db',
                                                   'django.contrib.sessions.backends.cache'):
                        from django.core.cache import cache
                        cache.clear()
            else:
                Visitor.objects.create(
                    user=request.user,
                    session_key=key_from_cookie
                )