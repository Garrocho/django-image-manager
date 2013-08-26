# -*- coding: utf-8 -*-
# @author: Charles Tim Batista Garrocho
# @contact: charles.garrocho@gmail.com
# @copyright: (C) 2013 Python Software Open Source

"""
This is the module of the application views.
"""

from django.http import HttpResponse
from django.utils import simplejson
from django.conf import settings
import manager
import mimetypes


def add(request):
    response, parameters = validate_request(request)
    if response.status_code == 204:
        if 'file' in request.FILES:
            if manager.add(request.FILES['file'], parameters['address'], parameters['name']):
                response.status_code = 200
    return response


def load(request):
    response, parameters = validate_request(request)

    if response.status_code == 204:
        image = manager.load(parameters['address'], parameters['name'])
        if image is not None:
            mimetype, encoding = mimetypes.guess_type(image)
            response = HttpResponse(mimetype=mimetype)
            response['Content-Disposition'] = 'attachment; filename=%s' % parameters['name']
            response.write(image)
            response.status_code = 200
    return response


def list(request):
    response, parameters = validate_request(request)

    if response.status_code == 204:
        lista_img = manager.list(parameters['address'], parameters['name'])
        if len(lista_img) > 0:
            response = HttpResponse(simplejson.dumps({'images': lista_img}), mimetype='application/json')
            response.encoding = 'utf-8'
            response.status_code = 200
    return response


def delete(request):
    response, parameters = validate_request(request)

    if response.status_code == 204:
        if manager.delete(parameters['address'], parameters['name']):
            response.status_code = 200
    return response


def validate_request(request):
    response = HttpResponse()
    response.status_code = 204
    parameters = None
    if request.method == settings.MANAGER_IMAGES_METHOD:
        if request.method == 'POST':
            if 'address' in request.POST and 'name' in request.POST:
                parameters = {'address':request.POST['address'], 'name':request.POST['name']}
            else:
                response.status_code = 401
        else:
            if 'address' in request.GET and 'name' in request.GET:
                parameters = {'address':request.GET['address'], 'name':request.GET['name']}
            else:
                response.status_code = 401
    else:
        response.status_code = 405
    return response, parameters
