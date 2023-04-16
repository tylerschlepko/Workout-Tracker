from app import db
from sqlalchemy.dialects.postgresql import JSON

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.Text, nullable=False)
    first_name = db.Column(db.String(20), nullable=True)
    last_name = db.Column(db.String(20), nullable=True)

    workouts = db.relationship('Workout', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.email}>'

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    workout = db.Column(JSON, nullable=False)
    minutes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Workout {self.id} for user {self.user_id}>'
