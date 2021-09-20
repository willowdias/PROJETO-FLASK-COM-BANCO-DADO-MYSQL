from itertools import repeat
from logging import error
from flask import Flask,render_template, request, session ,flash ,url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from werkzeug.utils import redirect
#######################tela login
app = Flask(__name__)
app.secret_key='123'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'cadastro'
mysql = MySQL(app)

@app.route('/login')
def login():
    return render_template("login.html")
@app.route("/autenticar",methods=['GET', 'POST'])
def logar():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        session['usuario logado']=request.form['username']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM usuario WHERE nome = %s AND senha = %s', (username, password))
        # Fetch one record and return result
        account = cursor.fetchone()
        
        
    if account:
        
        flash(request.form["username"] +  '   usuario logado  ')
        return redirect('/lista')
    else:
        
        flash('TENTE NOVAMENTE')
        return redirect ('/login')  

###############################################


@app.route('/lista')
def index():
    cur= mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT *FROM cliente")
    funcionarios = cur.fetchall()
    #print(funcionarios)
    return render_template("lista.html", funcionarios=funcionarios)
    
#@app.route("/lista" , methods=['GET', 'POST'])
#<form class="form-inline" method="POST" action="{{ url_for('test') }}">
#def test():
 #   select = request.form.get('comp_select')
  #  print(select)
   # return(str(select)) # just to see what select is


@app.route("/lista",methods=['GET', 'POST'])
def cadadastronovo():
    try:
        if request.method == "POST":
            #id= render_template['id-cliente']
            details = request.form
            nome = details['nome'].upper()
            endereco = details['end'].upper()
            cpf_vs = details['cpf'].replace('.','').replace('-','').lstrip()
            cidade = details['cidade'].upper()
            estado = details['estado'].upper()
            celular = details['numero'].upper()
            if nome=="" or endereco=="" or cpf_vs=="" or cidade=="" or estado=="" or   celular=="":
                
                flash('DADOS INCOMPLETO')
                return redirect(url_for("index"))
            
            else:
                cur= mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cur.execute("INSERT INTO  cliente (nome,endereco,cpf,cidade,estado,numero)VALUES('{}','{}','{}','{}','{}','{}')".format(nome,endereco,cpf_vs,cidade,estado,celular))
                
                #return redirect(url_for("index"))
                mensagem=("CADASTRO COM SUCESSO")
                if mensagem :
                    return render_template("lista.html", msg=mensagem)
                
                #return redirect(url_for("index"))                
                    
    except:
            flash('ERRO BANCO DADOS')
            return redirect(url_for("index"))
    
@app.route("/excluir/<int:id>",methods=['GET', 'POST'])
def excluir(id):
    cur= mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    
    cur.execute(f"DELETE FROM cliente WHERE id = {str(id)}")
    funcionarios = cur.fetchall()
    return redirect(url_for("index",funcionarios=funcionarios))
############
@app.route('/cadastro')
def cadastro():
      return render_template('cadastro.html')
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastracliente():
    if request.method == "POST":
        details = request.form
        firstName = details['username']
        lastName = details['password']
        fiemail=details['email']
        cur= mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("INSERT INTO  usuario (nome,senha,email)VALUES('{}','{}','{}')".format(firstName,lastName,fiemail))
        return "<span style='color:red; font-size:50px;'> CADASTRO COM SUCESSO</span>" 
if __name__ == "__main__":
    app.run(debug=True)