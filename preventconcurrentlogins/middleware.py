from django.contrib.sessions.models import Session
from django.conf import settings
from importlib import import_module

from preventconcurrentlogins.models import Visitor

engine = import_module(settings.SESSION_ENGINE)

class PreventConcurrentLoginsMiddleware(object):
    """
    Django middleware that prevents multiple concurrent logins..
    Adapted from http://stackoverflow.com/a/1814797 and https://gist.github.com/peterdemin/5829440
    """

    def process_request(self, request):
        if request.user.is_authenticated():
            key_from_cookie = request.session.session_key
            if hasattr(request.user, 'visitor'):
                session_key_in_visitor_db = request.user.visitor.session_key
                if session_key_in_visitor_db != key_from_cookie:
                    # Delete the Session object from database and cache
                    engine.SessionStore(session_key_in_visitor_db).delete()
                    request.user.visitor.session_key = key_from_cookie
                    request.user.visitor.save()
            else:
                Visitor.objects.create(
                    user=request.user,
                    session_key=key_from_cookie
                )
