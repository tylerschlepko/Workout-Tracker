import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from sqlalchemy.dialects.postgresql import JSON
from datetime import date


load_dotenv()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'postgresql://postgres:1qaz2wsx@localhost/worktrack'

db = SQLAlchemy(app)
migrate= Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
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
    minutes = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f'<Workout {self.id} for user {self.user_id}>'

@app.get('/add')
def add_users():
    # Create sample users
    user1 = User(email='john@example.com', password='johnspassword', first_name='John', last_name='Doe')
    user2 = User(email='jane@example.com', password='janespassword', first_name='Jane', last_name='Doe')

    # Add users to the database session
    db.session.add(user1)
    db.session.add(user2)

    # Commit the session to persist the users to the database
    db.session.commit()

    # Create sample workouts
    workout1 = Workout(date=date(2022, 1, 1), user_id=user1.id, workout={'exercise': 'Running', 'distance': 5}, minutes=30)
    workout2 = Workout(date=date(2022, 1, 2), user_id=user1.id, workout={'exercise': 'Swimming', 'laps': 10}, minutes=45)
    workout3 = Workout(date=date(2022, 1, 1), user_id=user2.id, workout={'exercise': 'Cycling', 'distance': 10}, minutes=60)

    # Add workouts to the database session
    db.session.add(workout1)
    db.session.add(workout2)
    db.session.add(workout3)

    # Commit the session to persist the workouts to the database
    db.session.commit()
    return 'Users and workouts added'

@app.get('/get')
def get_users():
    users = Workout.query.all()
    result = ''
    for user in users:
        result += f'{user.workout} - {user.id}'
    return result

@app.get('/api')
def test():
    test = {'name': 'Tyler', 'job' : 'SWE'}
    return jsonify(test)


if __name__ == '__main__':
    app.run(debug=True)

