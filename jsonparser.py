import json

f = open("sites.json", 'r')
l = open("espanhol.txt", 'w+')

parsed = json.loads(f.read())
for page in parsed['pages']:
	 l.write((page['results'][-1]["my_column"][-1])+'\n')