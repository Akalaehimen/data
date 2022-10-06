
from datetime import datetime
import email
from email.policy import default
import os
from re import S
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

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
    return render_template('index.html')
    # return '<h1>Welcome</h1


@app.route('/signup', methods=['GET', 'POST'])
def register():
    if request.method == 'post' :
        firstname = request.form.get('firstname')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
    
        student = Student.query.filter_by(firstname=firstname).first()

        if student:
            return redirect(url_for('register'))

        email_exists = Student.query.filter_by(email=email).first()
        if email_exists:
             return redirect(url_for('register'))

        password_hash = generate_password_hash(password)
        if password_hash:
             return redirect(url_for('register'))

        confirm = check_password_hash(confirm_password)
        if confirm:
            return redirect(url_for('register'))

        new_student = Student(firstname=firstname, email=email, password_hash=password_hash)
        db.session.add(new_student)
        db.session.commit

        return redirect(url_for('index'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')



@app.route('/logout')
def logout():
    pass

    
if __name__=='__main__':
    app.run(debug=True)

    




    