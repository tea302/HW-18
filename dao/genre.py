from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(Genre).get(uid)

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, genre_d):
        ent = Genre(*genre_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def update(self, genre_d):
        genre = self.get_one(genre_d.get("id"))

        genre.name = genre_d.get("name")

        self.session.add(genre)
        self.session.commit()

    def delete(self, uid):
        genre = self.get_one(uid)

        self.session.delete(genre)
        self.session.commit()