Django Handler Images
=====================
Application handler Images for django projects.


Installation:
-----------------------------

1. ``pip install git+git://github.com/CharlesGarrocho/django-handler-images``

Configuration:
-----------------------------

2. Add ``handler_images`` to your ``INSTALLED_APPS``

Usage:
-----------------------------

3. Include url ``handler_images`` to your ``urls.py`` in your app:

```py           
  urlpatterns = patterns('project_name',
    url(r'^handler_images/', include('handler_images.urls')),
  )
```

Contributors:
-----------------------------

* Charles Garrocho
