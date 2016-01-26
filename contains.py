lines_seen = set()
c = open("jogoscontem.txt", "w+")
with open("jogos.txt", "r") as j:
	for line in j:
		lines_seen.add(line)
with open("appsativos.txt", "r") as a:
	for line in a:
		if line in lines_seen:
			c.write(line)