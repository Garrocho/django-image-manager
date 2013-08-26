# -*- coding: utf-8 -*-
# @author: Charles Tim Batista Garrocho
# @contact: charles.garrocho@gmail.com
# @copyright: (C) 2013 Python Software Open Source

"""
This is the module of the application manager images.
"""

from django.conf import settings
import glob
import os


def add(image, address, name):
    '''
    records an image in the folder of the address passed as argument.
    '''
    try:
        path_dir = settings.MEDIA_IMAGES + address
        image_name, image_type = name.split('.')
        path = path_dir + '/' + image_name
        if not os.path.exists(path_dir):
            os.makedirs(path_dir)
        files = glob.glob(path + '*')
        len_files = len(files)
        if (len_files >= 1):
            path += '_' + str(len_files + 1) + '.' + image_type
        else:
            path += '_1.' + image_type
        destination = open(path, 'wb+')
        for chunk in image.chunks():
            destination.write(chunk)
        destination.close()
        return True
    except:
        return False


def load(address, name):
    '''
    loads an image from the folder name and the address passed as argument.
    '''
    path_image = settings.MEDIA_IMAGES + address + '/' + name
    if os.path.isfile(path_image):
    	return file(path_image, 'rb').read()
    else:
        return None


def list(address, name):
    '''
    several images in the folder list of the address and the name passed as argument.
    '''
    path_image = settings.MEDIA_IMAGES + address + '/' + name
    images = glob.glob(path_image + '*')
    list_images = []
    for image in images:
        list_images.append(image.split('/' + address + '/')[1])
    return list_images


def delete(address, name):
    '''
    delete an image from the folder address and name passed as argument.
    '''
    path_image = settings.MEDIA_IMAGES + address + '/' + name
    if os.path.isfile(path_image):
        os.remove(path_image)
        return True
    return False