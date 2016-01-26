import getEmail.py

f = open("listalinks.txt", 'r')

for x in range (0, 2):
	emails(f.readline())