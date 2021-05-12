from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'Secret Key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///idols.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

class idols(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    height = db.Column(db.String(50))
    age = db.Column(db.String(10))
    shows = db.Column(db.String(200))

    def __int__(self, name, height, age, shows):
        self.name = name
        self.height = height
        self.age = age
        self.shows = shows



@app.route('/')
def home():
    all_info = idols.query.all()
    return render_template('home.html', idols = all_info)

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        height = request.form['height']
        age = request.form['age']
        shows = request.form['shows']
        insert_data = idols(name=name, height=height, age=age, shows=shows)
        db.session.add(insert_data)
        db.session.commit()
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))


if __name__ == '__main__':
    app.run()
