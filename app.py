from flask import Flask, request, render_template, redirect, url_for
from hashlib import sha256
import secrets
import os

app = Flask(__name__)
DADOS = 'dados.txt'


@app.route('/')
def home():
    if os.path.exists(DADOS):
        return redirect(url_for('login'))
    return redirect(url_for('register'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']

        salt = secrets.token_hex(16)
        hash_registro = sha256((salt + senha).encode()).hexdigest()

        with open(DADOS, 'w') as f:
            f.write(f"{nome}\n{salt}\n{hash_registro}")

        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if not os.path.exists(DADOS):
        return redirect(url_for('register'))

    with open(DADOS, 'r') as f:
        nome_salvo = f.readline().strip()
        salt = f.readline().strip()
        hash_registro = f.readline().strip()

    msg = ''
    if request.method == 'POST':
        nome = request.form['nome']
        tentativa = request.form['senha']
        hash_tentativa = sha256((salt + tentativa).encode()).hexdigest()

        if nome == nome_salvo and hash_tentativa == hash_registro:
            return redirect(url_for('site', nome=nome))
        else:
            msg = '❌ Nome ou senha inválidos!'

    return render_template('login.html', msg=msg)


@app.route('/site')
def site():
    nome = request.args.get('nome', 'Visitante')
    return render_template('site.html', nome=nome)


if __name__ == '__main__':
    app.run(debug=True)
