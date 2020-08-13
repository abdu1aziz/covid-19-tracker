import requests, json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
countries_list = {'Andorra': 'ad',
'United Arab Emirates': 'ae',
'UAE': 'ae',
'Afghanistan': 'af',
'Albania': 'al',
'Armenia': 'am',
'Angola': 'ao',
'Antarctica': 'aq',
'Argentina': 'ar',
'Austria': 'at',
'Australia': 'au',
'Azerbaijan': 'az',
'Bosnia and Herzegovina': 'ba',
'Bangladesh': 'bd',
'Belgium': 'be',
'Burkina Faso': 'bf',
'Bulgaria': 'bg',
'Bahrain': 'bh',
'Burundi': 'bi',
'Benin': 'bj',
'Brunei-': 'bn',
'Bolivia, Plurinational State of': 'bo',
'Brazil': 'br',
'Bhutan': 'bt',
'Botswana': 'bw',
'Belarus': 'by',
'Belize': 'bz',
'Canada': 'ca',
'Congo, the Democratic Republic of the': 'cd',
'Central African Republic': 'cf',
'Congo': 'cg',
'Switzerland': 'ch',
'Cote d’Ivoire': 'ci',
'Chile': 'cl',
'Cameroon': 'cm',
'China': 'cn',
'Colombia': 'co',
'Costa Rica': 'cr',
'Cuba': 'cu',
'Cape Verde': 'cv',
'Cyprus': 'cy',
'Czech Republic': 'cz',
'Germany': 'de',
'Djibouti': 'dj',
'Denmark': 'dk',
'Dominican-Republic': 'do',
'Algeria': 'dz',
'Ecuador': 'ec',
'Estonia': 'ee',
'Egypt': 'eg',
'Western Sahara': 'eh',
'Eritrea': 'er',
'Spain': 'es',
'Ethiopia': 'et',
'Finland': 'fi',
'France': 'fr',
'Gabon': 'ga',
'United Kingdom': 'gb',
'UK': 'gb',
'Georgia': 'ge',
'French Guiana': 'gf',
'Ghana': 'gh',
'Greenland': 'gl',
'Gambia': 'gm',
'Guinea': 'gn',
'Equatorial Guinea': 'gq',
'Greece': 'gr',
'Guatemala': 'gt',
'Guam': 'gu',
'Guinea-Bissau': 'gw',
'Guyana': 'gy',
'Hong Kong': 'hk',
'Honduras': 'hn',
'Croatia': 'hr',
'Haiti': 'ht',
'Hungary': 'hu',
'Indonesia': 'id',
'Ireland': 'ie',
'Israel': 'il',
'India': 'in',
'Iraq': 'iq',
'Iran': 'ir',
'Iceland': 'is',
'Italy': 'it',
'Jamaica': 'jm',
'Jordan': 'jo',
'Japan': 'jp',
'Kenya': 'ke',
'Kyrgyzstan': 'kg',
'Cambodia': 'kh',
'Korea, Democratic People’s Republic of': 'kp',
'S.-Korea': 'kr',
'Kuwait': 'kw',
'Kazakhstan': 'kz',
'Lao People’s Democratic Republic': 'la',
'Lebanon': 'lb',
'Liechtenstein': 'li',
'Sri Lanka': 'lk',
'Liberia': 'lr',
'Lesotho': 'ls',
'Lithuania': 'lt',
'Luxembourg': 'lu',
'Latvia': 'lv',
'Libya': 'ly',
'Morocco': 'ma',
'Monaco': 'mc',
'Moldova, Republic of': 'md',
'Montenegro': 'me',
'Madagascar': 'mg',
'Macedonia, the former Yugoslav Republic of': 'mk',
'Mali': 'ml',
'Myanmar': 'mm',
'Mongolia': 'mn',
'Macao': 'mo',
'Mauritania': 'mr',
'Malta': 'mt',
'Mauritius': 'mu',
'Maldives': 'mv',
'Malawi': 'mw',
'Mexico': 'mx',
'Malaysia': 'my',
'Mozambique': 'mz',
'Namibia': 'na',
'Niger': 'ne',
'Nigeria': 'ng',
'Nicaragua': 'ni',
'Netherlands': 'nl',
'Norway': 'no',
'Nepal': 'np',
'New Zealand': 'nz',
'Oman': 'om',
'Panama': 'pa',
'Peru': 'pe',
'Papua New Guinea': 'pg',
'Philippines': 'ph',
'Pakistan': 'pk',
'Poland': 'pl',
'Puerto Rico': 'pr',
'Palestine, State of': 'ps',
'Portugal': 'pt',
'Paraguay': 'py',
'Reunion': 're',
'Romania': 'ro',
'Serbia': 'rs',
'Russia': 'ru',
'Rwanda': 'rw',
'Saudi Arabia': 'sa',
'Seychelles': 'sc',
'Sudan': 'sd',
'Sweden': 'se',
'Singapore': 'sg',
'Saint Helena, Ascension and Tristan da Cunha': 'sh',
'Slovenia': 'si',
'Slovakia': 'sk',
'Sierra Leone': 'sl',
'San Marino': 'sm',
'Senegal': 'sn',
'Somalia': 'so',
'Suriname': 'sr',
'Sao Tome and Principe': 'st',
'El Salvador': 'sv',
'Syrian Arab Republic': 'sy',
'Swaziland': 'sz',
'Chad': 'td',
'Togo': 'tg',
'Thailand': 'th',
'Tajikistan': 'tj',
'Timor-Leste': 'tl',
'Turkmenistan': 'tm',
'Tunisia': 'tn',
'Turkey': 'tr',
'Taiwan': 'tw',
'Tanzania, United Republic of': 'tz',
'Ukraine': 'ua',
'Uganda': 'ug',
'United States': 'us',
'USA': 'us',
'Uruguay': 'uy',
'Uzbekistan': 'uz',
'Holy See (Vatican City State)': 'va',
'Venezuela, Bolivarian Republic of': 've',
'Viet Nam': 'vn',
'Yemen': 'ye',
'Mayotte': 'yt',
'South Africa': 'za',
'Zambia': 'zm',
'Zimbabwe': 'zw'}

url = "https://covid-193.p.rapidapi.com/history"
country_list = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Anguilla', 'Antigua-and-Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia-and-Herzegovina', 'Brazil', 'British-Virgin-Islands', 'Brunei-', 'Bulgaria', 'Burkina-Faso', 'Cabo-Verde', 'Cambodia', 'Cameroon', 'Canada', 'CAR', 'Cayman-Islands', 'Chad', 'Channel-Islands', 'Chile', 'China', 'Colombia', 'Congo', 'Costa-Rica', 'Croatia', 'Cuba', 'Cura&ccedil;ao', 'Cyprus', 'Czechia', 'Denmark', 'Diamond-Princess-', 'Djibouti', 'Dominica', 'Dominican-Republic', 'DRC', 'Ecuador', 'Egypt', 'El-Salvador', 'Equatorial-Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Faeroe-Islands', 'Fiji', 'Finland', 'France', 'French-Guiana', 'French-Polynesia', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong-Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle-of-Man', 'Israel', 'Italy', 'Ivory-Coast', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Madagascar', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'MS-Zaandam', 'MS-Zaandam-', 'Myanmar', 'Namibia', 'Nepal', 'Netherlands', 'New-Caledonia', 'New-Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North-Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palestine', 'Panama', 'Papua-New-Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto-Rico', 'Qatar', 'R&eacute;union', 'Romania', 'Russia', 'Rwanda', 'S.-Korea', 'Saint-Kitts-and-Nevis', 'Saint-Lucia', 'Saint-Martin', 'San-Marino', 'Saudi-Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Singapore', 'Sint-Maarten', 'Slovakia', 'Slovenia', 'Somalia', 'South-Africa', 'Spain', 'Sri-Lanka', 'St.-Barth', 'St.-Vincent-Grenadines', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Trinidad-and-Tobago', 'Tunisia', 'Turkey', 'Turks-and-Caicos', 'U.S.-Virgin-Islands', 'UAE', 'Uganda', 'UK', 'Ukraine', 'Uruguay', 'USA', 'Uzbekistan', 'Vatican-City', 'Venezuela', 'Vietnam', 'Zambia', 'Zimbabwe']
headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "895c6f241emsh2dde6f986525553p1c22cdjsn2fefcaa3a4cd"
    }

app = Flask(__name__)
# C:\\Users\\Abdul Aziz\\Desktop\\proj-coronavirus\\
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///covid-19.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class covid_cases(db.Model):
	country_name    = db.Column(db.String(100))
	country_code    = db.Column(db.String(5), primary_key=True)
	new_cases       = db.Column(db.Integer, nullable=False, default='0')
	active_cases    = db.Column(db.Integer, nullable=False, default='0')
	critical_cases  = db.Column(db.Integer, nullable=False, default='0')
	recovered_cases = db.Column(db.Integer, nullable=False, default='0')
	new_deaths      = db.Column(db.Integer, nullable=False, default='0')
	total_deaths    = db.Column(db.Integer, nullable=False, default='0')

def makeData(countryName):
	querystring = {"country":countryName}
	response    = requests.request("GET", url, headers=headers, params=querystring)

	resp           = json.loads(response.text)
	country_name   = resp["response"][0]['country']
	new_cases      = resp["response"][0]['cases']['new']
	active_cases   = resp["response"][0]['cases']['active']
	critical_cases = resp["response"][0]['cases']['critical']
	recovered_cases= resp["response"][0]['cases']['recovered']
	new_deaths     = resp["response"][0]['deaths']['new']
	total_deaths   = resp["response"][0]['deaths']['total']

	covid_19 = covid_cases(country_name=country_name, country_code=countries_list[country_name], new_cases=new_cases, active_cases=active_cases, critical_cases=critical_cases, recovered_cases=recovered_cases, new_deaths=new_deaths, total_deaths=total_deaths)
	db.session.add(covid_19)

	
	# import csv
	# with open('covid-19-cases-1.csv', 'a+', newline='') as csvfile:
	#     covid_19_cases_writer = csv.writer(csvfile, delimiter=',')
	#     covid_19_cases_writer.writerow([country_name, new_cases, active_cases, critical_cases, recovered_cases, new_deaths, total_deaths])


# for country in country_list:
# 	try:
# 		makeData(country)
# 	except KeyError:
# 		continue

if __name__ == "__main__":
	app.run(debug=True)
