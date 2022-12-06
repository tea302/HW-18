from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO

from dao.service.director import DirectorService
from dao.service.genre import GenreService
from dao.service.movie import MovieService
from setup_db import db

director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)

director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)
