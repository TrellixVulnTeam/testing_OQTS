from flask import Flask , render_template ,redirect, session, url_for
from flask_wtf import FlaskForm
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from flask_sqlalchemy import SQLAlchemy
import os


app =Flask(__name__)
app.config['SECRET_KEY']='DRYTGVNBRVI'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'akash.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app = Flask(__name__)

class InfoForm(FlaskForm):
	fname = StringField('Enter your name')
	password = StringField('Enter your password')
	submit = SubmitField('submit')


class Account(db.Model):

	__tablename__ = 'details'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.Text)
	password = db.Column(db.Text)

	def __init__(self, username, password):
		self.username = username
		self.password = password

	def __repr__(self):
		return f"User with id {self.id} has Username {self.username} and Password {self.password}"






@app.route('/insert' , methods = ['GET','POST'])
def index():
	if form.validate_on_submit():

		form = InfoForm()
		fname = form.fname.data 
		password = form.password.data
		acc      = Account(fname , password)
		db.session.add(acc)
		db.session.commit()
		return redirect(url_for('inserted'))
	return render_template('insert.html' , form = form)


@app.route('/inserted')
def inserted():
	return render_template('inserted.html')


if __name__ == '__main__':
	app.run()