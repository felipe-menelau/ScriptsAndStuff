import sys
import requests

API_KEY = 'AIzaSyAkTwj3sMAyZwyjSNLgdOxBPbgIXwUZW1k'


def get_company_address(company, cities_to_match):
	"""
	Returns a company address if it matches any of the cities_to_match.
	"""
	
	base_url = "https://maps.googleapis.com/maps/api/place/autocomplete/json?"\
			   "input=%s&types=establishment&key=%s"
	
	search_url = base_url % (company, API_KEY)
	response = requests.get(search_url)
	print "[%s] GET %s" % (response.status_code, search_url)

	locations = []
	if response.status_code == 200:
		results = response.json()['predictions']

		for result in results:
			for term in result['terms']:
				if cities_to_match.get(term['value']):
					locations.append(result['description'])  
					break
	return locations

if __name__ == '__main__':
	cities_to_match = {
		'San Francisco': True,
		'San Mateo': True,
		'Berkeley': True,
		'Oakland': True,
		'Santa Clara': True,
		'San Jose': True,
		'Mountain View': True,
		'Palo Alto': True,
		'Los Gatos': True,
		'Fremont':True,
		'Hayward': True
	}
	a = "\n"
	f = open("rightcompanies.txt", "w+")
	with open("companies.txt", "r") as e:
		for line in e:
			company = line.rstrip()
			print get_company_address(company, cities_to_match)
			f.write(str(get_company_address(company, cities_to_match)))
			f.write(a)