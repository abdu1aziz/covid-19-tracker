from perday_v3 import *
db.create_all()

country_num = 0
print("Data Generation Started Please Wait....")
for country in country_list:
	try:
		makeData(country)
		country_num = country_num + 1
		print("[+] Country # %s" % (country_num))
	except KeyError:
		continue

db.session.commit()