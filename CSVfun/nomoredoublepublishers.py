import sys
import csv
from publisherexists import exists

def doubles (csvfile):
	ponto = ".csv"
	key = open("csvs/chave.txt", "r").readline()
	#-------------------
	#csvfile = "csvs/Top Apps (receita) Brazil W-Ads "
	csvfileout = csvfile + "EDITED"
	#-------------------

	f1 = open(csvfile + ponto, "r", errors="backslashreplace")
	f2 = open(csvfileout + ponto, "w", newline='')
	f3 = csv.reader(f1)
	visto = set()

	#Ler e escrever
	data = list(f3)
	writer = csv.writer(f2, quoting=csv.QUOTE_ALL)

	for i in range(len(data)):
		if exists(key, data[i][1]) and data[i][1] not in visto:
			visto.add(data[i][1])
			print("Removed %s" % str(data[i][1]))
		if data[i][1] not in visto:
			writer.writerow(data[i])
			visto.add(data[i][1])
	print ("Sucesso!")
	return True
 

if __name__ == "__main__":
	if doubles("csvs/Top Apps (receita) Brazil W-Ads "):
		print ("Sucesso final")
	else:
		print ("Fracasso")
