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

@app.route("/", defaults={'page_num': 1, 'filter_value': 'ac'})
@app.route("/<int:page_num>/<filter_value>")
def index(page_num, filter_value):
	filter_value = request.args.get("filter_value")
	if filter_value == "nc":
		filter_type = covid_cases.new_cases.desc()
	elif filter_value == "ac":
		filter_type = covid_cases.active_cases.desc()
	elif filter_value == "cc":
		filter_type = covid_cases.critical_cases.desc()
	elif filter_value == "nr":
		filter_type = covid_cases.new_recovered.desc()
	elif filter_value == "nd":
		filter_type = covid_cases.new_deaths.desc()
	elif filter_value == "td":
		filter_type = covid_cases.total_deaths.desc()
	else:
		filter_type = covid_cases.active_cases.desc()
	
	#covid_19_active = covid_cases.query.order_by(covid_cases.active_cases.desc()).limit(5)
	covid_19 = covid_cases.query.order_by(filter_type).paginate(per_page=25, page=page_num, error_out=True)
	return render_template('index.html', covid_19=covid_19) #, covid_19_active=covid_19_active)

@app.route("/countryLookup", methods=["POST"])
def countryLookup():
	country_name = request.form["country_name"].title()
	covid_19 = covid_cases.query.filter(covid_cases.country_name.ilike("%" + country_name + "%")).first()
	print(covid_19)
	if covid_19 is not None:
		covid_19_response = list([covid_19.country_name, covid_19.new_cases, covid_19.active_cases, covid_19.critical_cases, covid_19.recovered_cases, covid_19.new_deaths, covid_19.total_deaths])
		return jsonify({'covid_19': covid_19_response})
	error = "Invalid Country Name! Please Check Spelling and Try Again!"		
	return jsonify({'error': error})


@app.route("/newCases")
def newCases():
	new_cases = {}
	covid_19 = covid_cases.query.all()
	for cases in covid_19:
		try:
			country = countries_list[cases.country_name]
			new_cases.update({country: int(cases.new_cases)})
		except KeyError:
			continue

	custom_style = Style(background='#000000',  plot_background='#000000', foreground='#FFFFFF', foreground_strong='#FFFFFF', foreground_subtle='#FFFFFF', opacity='.6', opacity_hover='.9', transition='10ms ease-in', colors=('#fd7e14', '#CC0000', '#77B300'))
	new_cases_wMap = pygal.maps.world.World(style=custom_style)
	new_cases_wMap.title = 'New COVID-19 Cases (Latest Coronavirus Cases).'
	new_cases_wMap.add('New Cases', new_cases)
	nc_map = new_cases_wMap.render_data_uri()

	return render_template('newCases.html', nc_map=nc_map)

@app.route("/newDeaths")
def newDeaths():
	new_deaths = {}
	covid_19 = covid_cases.query.all()
	for cases in covid_19:
		try:
			country = countries_list[cases.country_name]
			new_deaths.update({country: int(cases.new_deaths)})
		except KeyError:
			continue

	custom_style = Style(background='#000000',  plot_background='#000000', foreground='#FFFFFF', foreground_strong='#FFFFFF', foreground_subtle='#FFFFFF', opacity='.6', opacity_hover='.9', transition='10ms ease-in', colors=('#CC0000', '#fd7e14', '#77B300'))
	new_cases_wMap = pygal.maps.world.World(style=custom_style)
	new_cases_wMap.title = 'New Deaths COVID-19 Cases (Latest Coronavirus Cases).'
	new_cases_wMap.add('New Deaths', new_deaths)
	nd_map = new_cases_wMap.render_data_uri()

	return render_template('newDeaths.html', nd_map=nd_map)


@app.route("/newRecovered")
def newRecovered():
	new_recovered ={}
	covid_19 = covid_cases.query.all()
	for cases in covid_19:
		try:
			country = countries_list[cases.country_name]
			new_recovered.update({country: int(cases.recovered_cases)})
		except KeyError:
			continue

	custom_style = Style(background='#000000',  plot_background='#000000', foreground='#FFFFFF', foreground_strong='#FFFFFF', foreground_subtle='#FFFFFF', opacity='.6', opacity_hover='.9', transition='10ms ease-in', colors=('#77B300', '#fd7e14', '#CC0000'))
	new_cases_wMap = pygal.maps.world.World(style=custom_style)
	new_cases_wMap.title = 'New Recovered COVID-19 Cases (Latest Coronavirus Cases).'
	new_cases_wMap.add('New Recovered', new_recovered)
	nr_map = new_cases_wMap.render_data_uri()	
	return render_template('newRecovered.html', nr_map=nr_map)


if __name__ == "__main__":
	app.run(debug=True)