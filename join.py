from validate_email import validate_email



f = open("valiemails.txt", 'w+')

with open("email2.txt", 'r') as e:
	for line in e:
		is_valid = validate_email(line.rstrip(),verify=True)
		if is_valid:
			f.write(line)