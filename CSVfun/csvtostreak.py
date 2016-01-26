import csv
from removedoubles import removedoubles


incsv = "Top Apps (receita) Brazil W-Ads .csv"

control = open("control.txt", "w+")
toread = open(incsv, "r")
read = csv.reader(toread)
data = list(read)
for i in range(len(data)):
	control.write(data[i][1])
	control.write("\n")
removedoubles("control.txt","control2.txt")