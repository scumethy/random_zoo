import os
from flask import Blueprint, send_file, abort

from app import db
from config import PATH_TO_IMAGES
from models.post import Request

history = Blueprint('history', __name__)


@history.route('/history')
def history_main():
    """ Обработчик запроса на историю предыдущих запросов.  """
    requests = db.session.query(Request).all()
    return str(requests)


@history.route('/history/static/<uuid>/')
def history_uuid(uuid):
    """ Обработчик запроса на одну запись из истории запросов. """
    record = db.session.query(Request).filter(Request.processed_image == uuid).first()
    try:
        filename = str(record.processed_image)
        files = list(filter(lambda x: x.startswith(filename), os.listdir(PATH_TO_IMAGES)))
        path_to_file = os.path.join(PATH_TO_IMAGES, files[0])
        return send_file(path_to_file)
    except AttributeError or IndexError or FileNotFoundError:
        abort(404)
