from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace("genres")


@genre_ns.route("/")
class GenresView(Resource):
    def get(self):
        g_ojects = genre_service.get_all()
        result = GenreSchema(many=True).dump(g_ojects)
        return result, 200


@genre_ns.route("/<int:uid>")
class GenreView(Resource):
    def get(self, uid):
        g_object = genre_service.get_one(uid)
        result = GenreSchema().dump(g_object)
        return result, 200