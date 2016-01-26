from sys import argvimport urllib

i = 0
txt = open("links.txt", 'r')


for i in range(0, 71):
	resource = urllib.urlopen(txt.readline())
	a = " Icone " + str(i) + ".png"
	output = open(a ,"wb")
	output.write(resource.read())
	output.close()