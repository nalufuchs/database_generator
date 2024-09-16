Aqui está o README adaptado conforme solicitado:

# Database Creation and Analysis Project

Este projeto em Python cria e gerencia um banco de dados relacional utilizando PostgreSQL. Ele inclui scripts para definir o esquema do banco de dados, popular com dados fictícios e realizar análises utilizando consultas SQL. Tudo é coordenado por um único arquivo `main.py`, que deve ser executado para rodar o projeto.

## Estrutura do Projeto

### Diretórios:

1. **`database/`**: Contém os scripts relacionados à criação e conexão do banco de dados.
   - **`create_database.py`**: Define o esquema do banco de dados usando SQLAlchemy.
   - **`db_connection.py`**: Configura a conexão com o banco de dados PostgreSQL usando SQLAlchemy.
   - **`populate_database.py`**: Utiliza a biblioteca Faker para gerar e inserir dados fictícios no banco de dados.
   
2. **`documents/`**: Contém a documentação visual e arquivos de dependências.
   - **`database_diagram.png`**: Esquema visual do banco de dados.
   - **`requirements.txt`**: Lista de dependências Python.

3. **`ETLs/`**: Contém scripts SQL e um pipeline para realizar ETLs no banco de dados.
   - **`pipeline.py`**: Executa os scripts SQL.
   - **`SQLqueries/`**: Diretório com as consultas SQL.
     - **`profitable_products_query.sql`**: Consulta SQL para criar uma tabela com os produtos mais rentáveis.
     - **`top_100_products_query.sql`**: Consulta SQL para criar uma tabela com os 100 produtos mais vendidos.
     - **`intersection_top100_and_profitable_products.sql`**: Consulta SQL para criar uma tabela com a intersecção dos produtos mais rentáveis e os 100 mais vendidos.

### Arquivos principais:

1. **`database_setup.py`**: Cria a conexão com o banco de dados.
2. **`data_population.py`**: Utiliza a função do `populate_database.py` para definir o número de linhas a ser populado no banco de dados.
3. **`etl_process.py`**: Processa os ETLs no diretório `SQLqueries`, criando novas tabelas de análise.

## Pré-requisitos

- Python 3.7 ou superior
- PostgreSQL
- Bibliotecas Python: `SQLAlchemy`, `Faker`, `psycopg2` (ou `psycopg2-binary`)

## Instalação

1. Clone o repositório para sua máquina local:

   ```bash
   git clone https://github.com/nalufuchs/database_generator
   cd database_generator
   ```

2. Crie um ambiente virtual e instale as dependências:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   cd documents
   pip install -r requirements.txt
   ```

3. Configure o banco de dados PostgreSQL e ajuste as configurações de conexão no arquivo `database/db_connection.py`, inserindo as configurações do seu banco de dados.

## Uso

1. **Criar o Banco de Dados**:

   Execute o arquivo `database_setup.py` para criar o banco de dados.
   ```bash
   python database_setup.py
   ```

2. **Popular o Banco de Dados**:

   Execute o arquivo `data_population.py` para inserir dados fictícios no banco de dados.
   ```bash
   python data_population.py
   ```
   Você pode personalizar o número de clientes, produtos e pedidos criados, alterando os parâmetros nas funções `create_customers`, `create_products` e `create_orders`:

   Esses parâmetros podem ser ajustados para simular diferentes cenários, conforme necessidade do usuário.


3. **Executar o ETL**:

   Execute o arquivo `etl_process.py` para realizar as consultas SQL e gerar as tabelas de análise.
   ```bash
   python etl_process.py
   ```

4. **Rodar todo o pipeline**:

   O script `main.py` executa o processo completo:
   - Cria o banco de dados e suas tabelas.
   - Insere dados fictícios.
   - Executa as consultas SQL e cria as tabelas de análise.

 
   Esses parâmetros podem ser ajustados para simular diferentes cenários.

## Esquema Visual do Banco de Dados

O diagrama abaixo representa o esquema do banco de dados criado:

![Database Schema](documents/database_diagram.png)

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma _issue_ ou enviar um _pull request_.