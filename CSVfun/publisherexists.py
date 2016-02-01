import requests

def exists(key, name):
	url = "https://www.streak.com/api/v1/search?query=" + name
	req = requests.get(url, auth=(key, ''))
	results = req.json()['results']
	if results == []:
		return False
	else:
		return True