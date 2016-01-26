j = open("linkstiago.txt", 'w')
g = open("coordenadas.txt", 'r')


for x in range (1, 1914):
	j.write("http://maps.google.com/maps?z=12&t=m&q=loc:" + g.readline())