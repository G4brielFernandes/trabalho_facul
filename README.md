# 🐱 Dá um 10 aí, professor!

Um mini projeto web simples feito em **Flask**, que exibe uma página de boas-vindas personalizada com uma imagem divertida de um gato pedindo nota 10 😸.

---

## 🚀 Tecnologias utilizadas
- Python 3  
- Flask  
- HTML5  
- Jinja2  

---

## 📁 Estrutura do projeto
projeto_gato/
│
├── app.py # Arquivo principal do Flask
├── static/
│ └── gatim.png # Imagem do gatinho
│
└── templates/
├── login.html # Página de login
└── bemvindo.html # Página de boas-vindas

yaml
Copiar código

---

## ⚙️ Como executar

1. **Clonar o repositório**
   ```bash
   git clone https://github.com/seuusuario/projeto_gato.git
   cd projeto_gato
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
