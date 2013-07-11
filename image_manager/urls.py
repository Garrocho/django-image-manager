from django.conf.urls import patterns, url

urlpatterns = patterns('image_manager',
    url(r'^add$', 'views.add', name='add'),
    url(r'^load$', 'views.load', name='load'),
    url(r'^list$', 'views.list', name='list'),
    url(r'^delete$', 'views.delete', name='delete'),
)
