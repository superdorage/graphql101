# Imports
from flask import Flask
from index import db

# app initialization
app = Flask(__name__)
app.debug = True

# Configs

# Modules

# Models
class User(db.Model):
    __tablename__ = 'users'

    uuid = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(256), index = True, unique = True)
    posts = db.relationship('Post', backref = 'author')

    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.Model):
    __tablename__ = 'posts'

    uuid = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(256), index = True)
    body = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('users.uuid'))

    def __repr__(self):
        return '<Post %r>' % self.title


# Schema Objects

# Routes


@app.route('/')
def index():
    return '<p> Hello World</p>'

if __name__ == '__main__':
    app.run()

