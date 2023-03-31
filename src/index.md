# Passo a Passo de Execução do Exercício 
1. Criação de Pasta com venv:

- Criar uma pasta vazia 
- Rodar o comando: 
`python -m venv`
- Acessar pasta Scripts:
`cd Scripts`
- Ativar a venv(Bash): 
`source activate

2. Criar um arquivo principal e importar as bibliotecas necessárias
  2.1. Instalar Flask: 
    `pip install Flask`

  2.2. Criar um servidor em flask: 
  `app = Flask(__name__)`
    `@app.route('/')`
    ` def index():`
      `return("Sem Erro")`

3. Instalação da SQLALchemy:
`pip install SQLAlchemy`

4. Criação de classe Base 
Inciialmente para criarmos a estrutura do nosso banco de dados criamos uma classe inicial de base na qual importamos "DeclarativeBase" do SQLAlchemy ORM. 

5. Em seguida criamos nossa estrutura principal da tabela contida no arquivo Game.py. 

6. Criada nossa estrutura de banco, criamos nossa engine que será responsável tanto pela criação do banco contendo as sessões, quando a criação de um endpoint responsável pela criação de novos registros no banco de dados. 

7. Criada a lista de registros de dados no banco que atua ao acionarmos o servidor em Flask. 

8. Para iniciar o servidor, basta rodar o comando: 
`flask --app main run ` 