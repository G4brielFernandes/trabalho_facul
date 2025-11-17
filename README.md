# Sistema de Login com Criptografia (Flask)

Projeto web desenvolvido em **Python (Flask)** que demonstra como funciona o processo de **registro e login com senha criptografada**, usando **hashes com salt** para proteger os dados do usuário.  
Além disso, exibe uma tela divertida de boas-vindas com o gatinho “ Dá um 10 aí, professor!” 

</div>
<h2> Equipe:</h2> 
<div>
  <table>
    <td align="center">
          <a href="https://github.com/AYSLANGADELHA">
            <img src="https://avatars.githubusercontent.com/u/169999742?v=4" alt="Ayslan Gadelha"
             width="100px"/>
            <br />
            <sub><b>Ayslan Gadelha</b></sub>
          </a>
      </td>
    <td align="center">
        <a href="https://github.com/G4brielFernandes" >
          <img src="https://avatars.githubusercontent.com/u/183325451?v=4" alt="Francisco Gabriel"
            width="100px" >
          <br>
          <sub><b>Francisco Grabriel</b></sub>
        </a>
      </td>
        <td align="center">
        <a href="https://github.com/gl0216016-hue" >
          <img src="https://avatars.githubusercontent.com/u/244214664?v=4" alt="Gabriel Lopes"
            width="100px" >
          <br>
          <sub><b>Grabriel Lopes</b></sub>
        </a>
      </td>
         <td align="center">
        <a href="https://github.com/kaishiix">
          <img src="https://avatars.githubusercontent.com/u/200096745?v=4" alt="Romulo Nascimento"
            width="100px" />
          <br />
          <sub><b>Romulo Nascimento</b></sub>
        </a>
      </td>
    </tr>
  </table>
</div>

---

##  Tecnologias utilizadas
- **Python 3**
- **Flask**
- **HTML5 + Jinja2**
- **Biblioteca hashlib (SHA-256)**
- **secrets** (para gerar salt seguro)

---

## Como o sistema funciona

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
- Se forem iguais, o login é aceito.

Esse processo impede que senhas sejam descobertas mesmo que o arquivo seja acessado — pois o hash é **irreversível** e o salt torna cada senha única.

---

##  Estrutura do projeto
O projeto é organizado em uma estrutura simples, composta pelos seguintes arquivos e diretórios:

app.py
Arquivo principal da aplicação Flask. Contém toda a lógica do servidor, incluindo rotas de registro, login, processamento de hash das senhas e exibição das páginas.

dados.txt
Arquivo utilizado para armazenar as informações dos usuários registrados. Nele são gravados o salt e o hash da senha, garantindo que nenhuma senha seja armazenada em texto puro.

/static
Diretório destinado a arquivos estáticos utilizados pela aplicação.

gatim.png: imagem exibida na página de boas-vindas.

/templates
Diretório que contém os arquivos HTML renderizados pelo Flask.
Inclui as seguintes páginas:

register.html: formulário de criação de nova conta.

login.html: página de autenticação do usuário.

bemvindo.html: página apresentada após o login bem-sucedido.


---

## Como executar

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

Copiar código
http://127.0.0.1:5000
