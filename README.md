## LEITURA DE ARQUIVOS CNAB

Bem vindos a API que vai automatizar a maneira com que voce le um arquivo CNAB. Basta carregar seu arquivo de texto CNAB e pronto, todos os dados sao exibidos na tela.

Para acessar um modelo de arquivo CNAB a ser lido, basta entrar no seguinte repositorio https://github.com/Kenzie-Academy-Brasil-Developers/desafio-backend-m6/blob/main/CNAB.txt

**LINGUAGENS**

- HTML
- PYTHON

**BIBLIOTECAS**

- DJANGO
- DJANGO REST FRAMEWORK

### CONFIGURANDO O AMBIENTE E INSTALANDO DEPENDENCIAS

Abra seu terminal na pasta do projeto e execute o seguinte comando `"python -m venv venv"`, isso ira criar um ambiente virtual em sua maquina local.

Em seguida, execute o comando `source venv/bin/activate`, isso ira fazer voce entrar no ambiente virtual criado.

E por ultimo, tambem em seu terminal, execute o comando `pip install -r requirements.txt`, esse ultimo comando, faz com que as dependencias do projeto sejam instaladas.

### RODANDO

Na pasta do projeto, apague o ".example" do arquivo ".env.example" e preencha com suas informaçoes. Lembre-se que iremos utilizar um banco de dados postgreSQL.

Agora vamos persistir as migrations no seu banco criado com os seguintes comando `python manage.py makemigrations` e depois `python manage.py migrate`

Abra mais uma vez seu terminal, e execute o comando `python manage.py types` para criar em seu banco, valores ja pre definidos

E por ultimo, vamos rodar o nosso projeto executando o comando `python manage.py runserver`
