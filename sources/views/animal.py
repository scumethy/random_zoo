import requests
from flask import Blueprint, send_file

from utils import process_image

animal = Blueprint('animal', __name__)


@animal.route('/animal/cat')
def animal_cat():
    """ Обработчик запроса обработанного изображения кота.
    Сервис 'http://aws.random.cat/' не работал и я использовал тот же,
    что и для собак.
    """
    response = requests.get("http://shibe.online/api/cats")
    download_link = str(response.content)[4:-3]
    path_to_image = process_image(download_link, 'cat')
    return send_file(path_to_image)


@animal.route('/animal/dog')
def animal_dog():
    """ Обработчик запроса обработанного изображения кота. """
    response = requests.get("http://shibe.online/api/shibes")
    download_link = str(response.content)[4:-3]
    path_to_image = process_image(download_link, 'dog')
    return send_file(path_to_image)


@animal.route('/animal/fox')
def animal_fox():
    """ Обработчик запроса обработанного изображения кота. """
    response = requests.get("https://randomfox.ca/floof/")
    download_link = eval(response.content)['image'].replace('\\', '')
    path_to_image = process_image(download_link, 'fox')
    return send_file(path_to_image)
