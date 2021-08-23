from app import db

class Ytchannels(db.Model):
    __tablename__ = 'ytchannels'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(1024))
    quote = db.Column(db.String(1024))
    url = db.Column(db.String(1024))
    tags = db.Column(db.String(1024))
    born_date = db.Column(db.String(1024))
    born_location = db.Column(db.String(1024))
    description = db.Column(db.String(1024))

    def __repr__(self):
        return '<Ytchannels {}>'.format(self.author)