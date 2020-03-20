from phonebook import app, db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from phonebook import login
from flask_login import UserMixin

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False, unique=True)
    phone = db.Column(db.String(256), nullable=False)
    address = db.Column(db.String(150), nullable=False, unique=True)
    # post = db.relationship('Post', backref='author')

    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = self.set_password(phone)

    def __repr__(self):
        # repeater, similar to str method, easier to use inside model
        return f"{self.name} has been created with {self.address}"

    def set_password(self, phone):
        self.pw_hash = generate_password_hash(phone)
        return self.pw_hash


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    address = db.Column(db.String(3000), nullable=False)
    date_created = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, name, address, user_id):
        self.name = name
        self.address = address
        self.user_id = user_id

    def __repr__(self):
        return f"The contact info is for: {self.name} and the user is {self.user_id}"
