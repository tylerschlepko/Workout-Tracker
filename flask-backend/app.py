import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash


load_dotenv()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'postgresql://postgres:1qaz2wsx@localhost/worktrack'

db = SQLAlchemy(app)


@app.get('/api')
def test():
    test = {'name': 'Tyler', 'job' : 'SWE'}
    return jsonify(test)


if __name__ == '__main__':
    app.run(debug=True)

