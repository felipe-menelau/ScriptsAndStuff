
def removedoubles(inf, outf):
	lines_seen = set()
	outfile = open(outf, "w+")
	for line in open(inf, "r"):
		if line not in lines_seen:
			outfile.write(line)
			lines_seen.add(line)
	outfile.close()