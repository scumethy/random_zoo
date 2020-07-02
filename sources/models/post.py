from datetime import datetime

from app import db


class Request(db.Model):
    """ Модель, предписывающая параметры заиси запросов животных в БД. """
    id = db.Column(db.Integer(), primary_key=True)
    animal_type = db.Column(db.String(30), nullable=False)
    processed_image = db.Column(db.String(), unique=True, nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return "<{}:{} {} - {}>".format(self.id, self.animal_type, self.processed_image, self.created_on)
