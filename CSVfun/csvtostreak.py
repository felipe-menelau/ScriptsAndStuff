import requests
import sys
import csv
import json
from nomoredoublepublishers import doubles
#############################################
key = open("csvs/chave.txt", "r").readline()
pkey = open("csvs/pchave.txt", "r").readline()
#############################################
csvf = "csvs/Top Apps (receita) Brazil W-Ads "
csvfileout = csvf + "EDITED"
ponto = ".csv"


def createboxes(key, pkey):
	f = open(csvfileout + ponto, "r", encoding="latin-1", errors="backslashreplace")
	f1 = csv.reader(f)
	data = list(f1)
	for i in range(1, len(data)):
		r = requests.put("https://www.streak.com/api/v1/pipelines/" + pkey + "/boxes?name=" + data[i][1], auth=(key, ''))
		if r.status_code is 200:
			print("Publisher %s inserido" % data[i][1])
			editbox(key, pkey, r.json()['boxKey'], i)
		else:
			print("Falhou, cod %s" % str(r.status_code))
	f.close()

def editbox(key, pkey, boxkey, number):
	f = open(csvfileout + ponto, "r", encoding="latin-1", errors="backslashreplace")
	f1 = csv.reader(f)
	data = list(f1)
	appname = {}
	contactemail = {}
	link = {}
	sdk = {}
	appname['value'] = data[number][0]
	contactemail['value'] = data[number][12]
	link['value'] = data[number][3]
	sdk['value'] = data[number][9]
	appname_json = json.dumps(appname)
	contactemail_json = json.dumps(contactemail)
	link_json = json.dumps(link)
	sdk_json = json.dumps(sdk)
	r = requests.post("https://www.streak.com/api/v1/boxes/" + boxkey + "/fields/1003", auth=(key, ''), data =appname_json, headers= {"Content-Type":"application/json"})
	print(r.status_code)
	r = requests.post("https://www.streak.com/api/v1/boxes/" + boxkey + "/fields/1004", auth=(key, ''), data =contactemail_json, headers= {"Content-Type":"application/json"})
	print(r.status_code)
	r = requests.post("https://www.streak.com/api/v1/boxes/" + boxkey + "/fields/1006", auth=(key, ''), data =link_json, headers= {"Content-Type":"application/json"})
	print(r.status_code)
	r = requests.post("https://www.streak.com/api/v1/boxes/" + boxkey + "/fields/1009", auth=(key, ''), data =sdk_json, headers= {"Content-Type":"application/json"})
	print(r.status_code)

if __name__ == "__main__":
	doubles(csvf)
	createboxes(key, pkey)
