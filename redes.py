import time
import BaseHTTPServer
import html
from os import curdir, sep
import cgi


HOST_NAME = ''
NUMERO_PORTA = 8081 


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	#Pra cuidar do HEAD
	def do_HEAD(s):
		s.send_response(200)
		s.send_header('Content-type','text/html')
		s.end_headers()
	
	#Pra cuidar do GET
	def do_GET(s):
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
		s.wfile.write("<html><head><title>Teste</title></head>")
		s.wfile.write('<form action="/my-handling-form-page" method="post">')
		s.wfile.write("<div>")
		s.wfile.write('Nome:<br>')
		s.wfile.write('<input type="text" value="name" />')
		s.wfile.write("<br></div>")
		s.wfile.write('<input type="submit" value="Submit">')
		s.wfile.write("</form>")
		s.wfile.write("</div>")
		s.wfile.write("</html>")

	#Para cuidar do POST
	def do_POST(s):
        # Parsear o que foi digitado no post usando a biblioteca CGI
		form = cgi.FieldStorage(
			fp=s.rfile, 
			headers=s.headers,
			environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':s.headers['Content-Type'],
					})
		content_len = int(s.headers.getheader('content-length', 0))
		post_body = s.rfile.read(content_len)

		#Comeca a resposta
		s.send_response(200)
		s.end_headers()
		s.wfile.write('Cliente: %s\n' % str(s.client_address))
		s.wfile.write('Agente: %s\n' % str(s.headers['user-agent']))
		s.wfile.write('Caminho: %s\n' % s.path)
		s.wfile.write('Todos os headers:\n')
		s.wfile.write(s.headers)
		

		for field in form.keys():
			field_item = form[field]
			if field_item.filename:
				file_data = field_item.file.read()
				file_len = len(file_data)
				del file_data
				s.wfile.write('\tUploaded %s as "%s" (%d bytes)\n' % \
					(field, field_item.filename, file_len))
			else:
				s.wfile.write('\t%s=%s\n' % (field, form[field].value))
			return

			
if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, NUMERO_PORTA), MyHandler)
    print time.asctime(), " - %s:%s" % (HOST_NAME, NUMERO_PORTA)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "- %s:%s" % (HOST_NAME, NUMERO_PORTA)
    print time.asctime(), "- %s:%s" % (HOST_NAME, NUMERO_PORTA)