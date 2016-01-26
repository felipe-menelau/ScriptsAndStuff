import webbrowser, sys, pyperclip

#mandar por argumento
if len(sys.argv) > 1:
	address = ' '.join(sys.argv[1:])
else:
	#pegar do ctrlc
	address = pyperclip.paste()
	
webbrowser.open('https://accounts.inlocomedia.com/pt-BR/admin/users/impersonate?email=' + address)
