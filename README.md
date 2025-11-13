# 🔐 Grupo 2 - Sistema de Login com Criptografia (Flask)

Projeto web desenvolvido em **Python (Flask)** que demonstra como funciona o processo de **registro e login com senha criptografada**, usando **hashes com salt** para proteger os dados do usuário.  
Além disso, exibe uma tela divertida de boas-vindas com o gatinho “🐱 Dá um 10 aí, professor!” 😸

---

## 🚀 Tecnologias utilizadas
- **Python 3**
- **Flask**
- **HTML5 + Jinja2**
- **Biblioteca hashlib (SHA-256)**
- **secrets** (para gerar salt seguro)

---

## 🧠 Como o sistema funciona

1. O usuário acessa a página **/register** e cria sua conta.  
2. A senha digitada é **criptografada com SHA-256** e combinada com um **salt aleatório** (um código único gerado a cada registro).  
3. Esses dados são salvos em um arquivo `dados.txt` no formato:
salt
hash_da_senha

yaml
Copiar código
4. Quando o usuário tenta fazer login:
- O sistema lê o `salt` e o `hash` salvos.  
- Aplica o mesmo processo de hash (`sha256(salt + senha_digitada)`).  
- Compara o resultado com o hash armazenado.  
- Se forem iguais, o login é aceito ✅.

Esse processo impede que senhas sejam descobertas mesmo que o arquivo seja acessado — pois o hash é **irreversível** e o salt torna cada senha única.

---

## 📁 Estrutura do projeto
projeto_grupo2/
│
├── app.py # Arquivo principal do Flask
├── dados.txt # Arquivo onde as senhas (com hash) são armazenadas
│
├── static/
│ └── gatim.png # Imagem do gatinho
│
└── templates/
├── register.html # Página de registro de nova conta
├── login.html # Página de login
└── bemvindo.html # Página de boas-vindas

yaml
Copiar código

---

## ⚙️ Como executar

1. **Clonar o repositório**
   ```bash
   git clone https://github.com/seuusuario/projeto_grupo2.git
   cd projeto_grupo2
Criar ambiente virtual (opcional)

bash
Copiar código
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate   # Linux
Instalar dependências

bash
Copiar código
pip install flask
Executar o servidor

bash
Copiar código
python app.py
Abrir no navegador

cpp
Copiar código
http://127.0.0.1:5000
