Django Image Manager
====================
Image manager for django projects

Installation:
-----------------------------
1. ``pip install git+git://github.com/CharlesGarrocho/django-image-manager``

Configuration:
-----------------------------
1. Add ``image_manager`` to your ``INSTALLED_APPS`` in ``settings.py``;

2. Add the path ``MEDIA_ROOT`` and ``MEDIA_IMAGES`` in ``settings.py``:
```py           
    MEDIA_ROOT = '/home/charles/webapps/media/data/'
    MEDIA_IMAGES = MEDIA_ROOT + 'images/'
```

3. Defines the type of method will be ``GET`` or ``POST`` in ``settings.py``:
```py           
    MANAGER_IMAGES_METHOD = 'GET'
```

Usage:
-----------------------------

1. Include url ``image_manager`` to ``urls.py`` in your app:
```py           
    urlpatterns = patterns('project_name',
        url(r'^image_manager/', include('image_manager.urls')),
    )
```

2. Parameters to be used are: 
``address`` what is the address of the image folder and ``name`` what is the name of the image. 

Contributors:
-----------------------------
* Charles Garrocho
