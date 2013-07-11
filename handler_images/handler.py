#coding: utf-8
from django.conf import settings
import glob
import os


def add(image, address, name):
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
    path_image = settings.MEDIA_IMAGES + address + '/' + name
    if os.path.isfile(path_image):
    	return file(path_image, 'rb').read()
    else:
        return None


def list(address, name):
    path_image = settings.MEDIA_IMAGES + address + '/' + name
    images = glob.glob(path_image + '*')
    list_images = []
    for image in images:
        list_images.append(image.split('/' + address + '/')[1])
    return list_images


def delete(address, name):
    path_image = settings.MEDIA_IMAGES + address + '/' + name
    if os.path.isfile(path_image):
        os.remove(path_image)
        return True
    return False