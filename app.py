from flask import Flask
from flask_restx import Api
from sqlalchemy.testing import db

from config import Config
from dao.views.director import director_ns
from dao.views.genre import genre_ns
from dao.views.movie import movie_ns


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object((config_obj))
    register_extensions(app)
    return app


def register_extensions(app):
    api = Api(app)
    db.init.app(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=False)



