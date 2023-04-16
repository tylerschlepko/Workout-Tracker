DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS workouts CASCADE;

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    email VARCHAR,
    password TEXT,
    first_name VARCHAR(20),
    last_name VARCHAR(20)
);

CREATE TABLE workouts(
    id SERIAL PRIMARY KEY,
    date DATE,
    user_id INT,
    workout JSON,
    minutes INT,
    CONSTRAINT fk_user_id
        FOREIGN KEY(user_id)
            REFERENCES users(id)
);