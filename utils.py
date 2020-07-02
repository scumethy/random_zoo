import io
import os
import uuid
import requests
import PIL

from flask import abort
from PIL import Image, ImageFilter
from sqlalchemy.exc import IntegrityError

from app import db
from config import PATH_TO_IMAGES
from models.post import Request


def get_mime(link):
    """ Функция, возвращающая расширение изображения. """
    try:
        mime = link.split('.')[-1]
    except IndexError:
        mime = 'jpg'
    return mime


def get_unique_filename():
    """ Функция, возвращающая уникальный uuid номер. """
    return str(uuid.uuid4())


def filter_image(image_binary):
    """ Функция, применяющая фильтр на изображение. """
    image = PIL.Image.open(io.BytesIO(image_binary)).convert('RGB')
    blurred_image = image.filter(ImageFilter.BLUR)
    return blurred_image


def process_image(download_link, animal):
    """ Функция, производящая:
        запрос на внешний ресурс,
        сохранение файла в память,
        добавление новой записи в БД.
    """
    image_binary = requests.get(download_link).content
    filtered_image = filter_image(image_binary)

    uuid_filename = get_unique_filename()
    file_type = get_mime(download_link)
    filename = f'{uuid_filename}.{file_type}'
    file_path = os.path.join(PATH_TO_IMAGES, filename)
    filtered_image.save(file_path)

    try:
        db.session.add(Request(
            animal_type=animal,
            processed_image=uuid_filename,
        ))
        db.session.commit()
    except IntegrityError:
        abort(500)

    return file_path
