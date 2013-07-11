Django Image Manager
====================
Application manager images for django projects.


Installation:
-----------------------------

1. ``pip install git+git://github.com/CharlesGarrocho/django-image-manager``

Configuration:
-----------------------------

2. Add ``image_manager`` to your ``INSTALLED_APPS``

Usage:
-----------------------------

3. Include url ``image_manager`` to your ``urls.py`` in your app:

```py           
  urlpatterns = patterns('project_name',
    url(r'^image_manager/', include('image_manager.urls')),
  )
```

Contributors:
-----------------------------

* Charles Garrocho
