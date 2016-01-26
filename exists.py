import httplib
import urllib2

def checkurl(url):
	try:
		urllib2.urlopen(url)
		return True
	except urllib2.URLError:
		return False
	
f = open("espanholsredirect.txt", 'r')
l = open("espanholsvalidos.txt", 'w+')
for x in range(0, 102):
	c = f.readline()
	if checkurl(c):
		l.write(c)
	else:
		print ("URL invalida")