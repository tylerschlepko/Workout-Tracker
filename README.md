# Workout Tracker

Workout Tracker is a web application for tracking and logging your workouts. Built with Vite, React, Python, Flask, and PostgreSQL, it helps you stay accountable for your workouts by keeping a record of your progress in the database.

## Features

- Add, edit, and delete workouts
- Log your workout data (sets, reps, weight, etc.)
- Visualize workout progress over time
- Authentication and user management
- Personalized workout plans and recommendations

## Prerequisites

Before getting started, make sure you have the following tools installed on your system:

- [Node.js](https://nodejs.org/en/) (v14.x or later)
- [Python](https://www.python.org/) (v3.6 or later)
- [PostgreSQL](https://www.postgresql.org/) (v10.x or later)

## Getting Started

### Clone the repository

```
$ git clone https://github.com/tylerschlepko/workout-tracker.git
$ cd workout-tracker
````

### Set up the frontend
Navigate to the react directory and install the dependencies:

```
cd react
npm install
```

Run the development server
```
npm run dev
```

The frontend will be available at http://localhost:3000.

### Set up the backend
Navigate to the flask-backend directory, create a virtual environment, and install the dependencies:

```
cd flask-backend/
```

Create a .env file in the backend directory with the following content (replace the placeholders with your PostgreSQL credentials):
```
DATABASE_URL=postgresql://username:password@localhost/db_name
```

To start the development server, run:
```
flask run
```
The backend API will be available at http://localhost:5000.

### Usage
Navigate to http://localhost:3000 in your browser, create an account or log in, and start tracking your workouts!

### Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.

### License
MIT
