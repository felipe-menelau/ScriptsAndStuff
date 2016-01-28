import csv

ponto = ".csv"

#-------------------
csvfile = "csvs/Top Apps (receita) Brazil W-Ads "
csvfileout = csvfile + "DOIS"
#-------------------

f1 = open(csvfile + ponto, "r", errors="backslashreplace")
f2 = open(csvfileout + ponto, "w", newline='')
f3 = csv.reader(f1)
visto = set()

#Ler e escrever
data = list(f3)
writer = csv.writer(f2, quoting=csv.QUOTE_ALL)

for i in range(len(data)):
	if data[i][1] not in visto:
		writer.writerow(data[i])
		visto.add(data[i][1])
