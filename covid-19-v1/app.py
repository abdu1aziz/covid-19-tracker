from flask import Flask, render_template, url_for, redirect, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from sqlalchemy import asc
from sqlalchemy import func as func


from assets.list_of_countries import countries_list
import pygal
from pygal.style import Style



app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///covid-19.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class covid_cases(db.Model):
	country_name    = db.Column(db.String(100), primary_key=True)
	country_code    = db.Column(db.String(5))
	new_cases       = db.Column(db.Integer, nullable=False, default='0')
	active_cases    = db.Column(db.Integer, nullable=False, default='0')
	critical_cases  = db.Column(db.Integer, nullable=False, default='0')
	recovered_cases = db.Column(db.Integer, nullable=False, default='0')
	new_deaths      = db.Column(db.Integer, nullable=False, default='0')
	total_deaths    = db.Column(db.Integer, nullable=False, default='0')

@app.route("/")
def index():

	covid_19 = covid_cases.query.order_by(covid_cases.active_cases.desc()).all()
	return render_template('index.html', covid_19=covid_19)

@app.route("/getNewData")
def getNewData():
	covid_19 = covid_cases.query.order_by(covid_cases.active_cases.desc()).all()
	#print(covid_19)
	countryList = []
	for c in countryList:
		countryList.append(c)
	return jsonify({'data': countryList})

@app.route("/countryLookup", methods=["POST"])
def countryLookup():
	country_name = request.form["country_name"]
	covid_19 = covid_cases.query.filter_by(country_name=country_name).first()
	print(covid_19)
	if covid_19 is not None:
		covid_19_response = list([covid_19.country_name, covid_19.new_cases, covid_19.active_cases, covid_19.critical_cases, covid_19.recovered_cases, covid_19.new_deaths, covid_19.total_deaths])
		return jsonify({'covid_19': covid_19_response})
	error = "Invalid Country Name! Please Check Spelling and Try Again!"		
	return jsonify({'error': error})


if __name__ == "__main__":
	app.run(debug=True)