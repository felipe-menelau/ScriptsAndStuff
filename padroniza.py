
dest = "textfiles/tiago2.txt"
w = open("textfiles/saidaPadrao.txt", 'w')
with open(dest, 'r') as f:
	for i in range(len(f.read())):
		strin = f.readline()
		strin.replace(',', '.')
		strin.replace('\t', ',')
		w.write(strin + '\n')