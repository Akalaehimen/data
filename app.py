from datetime import datetime
import email
from email.policy import default
import os
from re import S
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ...

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.Text, nullable=False )
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    bio = db.Column(db.Text)

    def __repr__(self):
        return f'<Student {self.firstname}>'
        
        # ...
    @app.route('/')
    def index():
    #    student = Student.query.filter_by(email = email).first()
        return render_template('base.html')
        
    

    @app.route('/login')
    def login(): 
        pass

    @app.route('/signup')
    def signup():
        pass

    
    if __name__=='__main__':
     app.run(debug=True)

    













    