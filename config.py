import os

# Путь к файлу БД
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.getcwd(), 'zoo.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Путь к папке для хранения изображений
PATH_TO_IMAGES = os.path.join(os.getcwd(), 'images')
