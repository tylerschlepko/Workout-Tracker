from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1qaz2wsx@localhost/worktrack'

@app.get('/api')
def test():
    test = {'name': 'Tyler', 'job' : 'SWE'}
    return jsonify(test)


if __name__ == '__main__':
    app.run(debug=True)