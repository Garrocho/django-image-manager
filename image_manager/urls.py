# -*- coding: utf-8 -*-
# @author: Charles Tim Batista Garrocho
# @contact: charles.garrocho@gmail.com
# @copyright: (C) 2013 Python Software Open Source

"""
This is the module urls for navigation in the application.
"""

from django.conf.urls import patterns, url

urlpatterns = patterns('image_manager',
    url(r'^add$', 'views.add', name='add'),
    url(r'^load$', 'views.load', name='load'),
    url(r'^list$', 'views.list', name='list'),
    url(r'^delete$', 'views.delete', name='delete'),
)
