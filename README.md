django-preventconcurrentlogins
==============================

Django middleware that prevents multiple concurrent logins. If a user is already logged into the Django application and
tries to log in somewhere else, the previous session is deleted.


This package is based on code from http://stackoverflow.com/a/1814797 and https://gist.github.com/peterdemin/5829440.


Usage
-----------

1. Add "preventconcurrentlogins" to your INSTALLED_APPS settings like this::

    ```python
        INSTALLED_APPS = {        
            ...
                'preventconcurrentlogins',
        }
    ```
    

2. Add "preventconcurrentlogs.middleware.PreventConcurrentLoginsMiddleware" to MIDDLEWARE_CLASSES::

    ```python
        MIDDLEWARE_CLASSES = {        
            ...
                'preventconcurrentlogs.middleware.PreventConcurrentLoginsMiddleware',
        }
    ```
    

2. Run `python manage.py migrate` to create the visitor model that is used to track a users currently active session
key.
