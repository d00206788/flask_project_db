from flask import Flask, render_template, jsonify
import psycopg2
import os

app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/flask_db'
db = SQLAlchemy(app)

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/skills.html')
def gallery():
    return render_template('skills.html')

@app.route('/projects.html')
def projects():
    return render_template('projects.html')

@app.route('/extra.html')
def extra():
    return render_template('extra.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
 app.run(debug = True)

 class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

# Create the database tables
db.create_all()

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [{'id': user.id, 'username': user.username} for user in users]
    return jsonify({'users': user_list})


 