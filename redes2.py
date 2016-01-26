from bottle import route, run, get, put, post, request, delete, template
import random

PORTA = 8081
IP = '192.168.2.139'

@route('/')
def inicial():
	return "Trabalho de Redes, bem vindo"

@route('/olar')
def olar():
    return "Olar, tudo bem?"
	
@get('/olar/<name>')
def cumprimentar(name = 'Estranho'):
	return template('Olar {{name}}, como vai voce?', name = name)

@get('/login')
def login():
    return '''
        <form action="/login" method="post">
            Usuario: <input name="usuario" type="text" />
            Senha: <input name="senha" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

def check_login(usuario, senha):
	if 5 >= random.randint(0, 10):
		return True
	else: return False
	
@post('/login')
def do_login():
    usuario = request.forms.get('usuario')
    senha = request.forms.get('senha')
    if check_login(usuario, senha):
        return "<p>Tava certo, tu logou</p>"
    else:
        return "<p>Nope. Tente de novo</p>"
		
receitas = []
		
@get('/receitas/')
def lista_receitas():
    return "LISTA " + str(receitas)

@route('/receitas/colocar')
def receitas_show():
	return '''
		<form action="/receitas/colocar" method="post">
			Receita: <input name="receita" type="text" />
			<input value="Colocar" type="submit" />
			</form>
			<form action="/receitas/tirar" method="post">
			<input value="Tirar" type="submit" />
			</form>
			'''

@post('/receitas/colocar')
def receitas_colocar(name = 'Receita'):
	name = request.forms.get('receita')
	receitas.append(name)
	return "SALVAR RECEITA " + name

@post('/receitas/tirar')
def receitas_tirar(name = 'Receita'):
	name = request.forms.get('receita')
	receitas.pop()
	return "DELETAR RECEITA " + name

@delete('/receitas/<name>')
def recipe_delete( name="Receita" ):
	receitas.remove(name)
	return "DELETAR RECEITA " + name

@put('/receitas/<name>')
def recipe_save( name="Receita" ):
	receitas.append(name)
	return "SALVAR RECEITA " + name
	
run(host=IP, port=PORTA, debug=True)