from app import app, db
from models import User, Workout
from datetime import date

with app.app_context():
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
