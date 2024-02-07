import pyodbc
import pandas as pd
import warnings
from decouple import config

# Os dados do banco de dados
DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_NAME = config('DB_NAME')

# Para não precisar usar  o SQLAlchmey
warnings.simplefilter(action='ignore', category=UserWarning)

# Iniciando a conexão com o banco
conectar_banco = pyodbc.connect(f'DSN={DB_NAME};UID={DB_USER};PWD={DB_PASSWORD}')

# Iniciando a query
cursor = conectar_banco.cursor()

# Executar uma query para obter as tabelas
cursor.execute("SHOW TABLES")

# Para recuperar os dados
tabelas = cursor.fetchall()

# Para imprimir cada tabela dentro do banco
for tabela in tabelas:
    print(tabela[0])

# Query para juntar as informações do banco de dados
query = '''SELECT
	p.ID_Pedido,
    p.Data_Venda,
	l.Loja,
    pr.Nome_Produto,
	pr.Marca_Produto,
    c.Nome,
    c.Sobrenome,
    p.Qtd_Vendida,
    p.Receita_Venda,
    p.Custo_Venda,
    pr.Preco_Unit,
    pr.Custo_Unit,
    l.Gerente,
    l.Endereco,
    l.Num_Funcionarios
FROM
	pedidos p
INNER JOIN
	produtos pr ON pr.ID_Produto=p.ID_Produto
INNER JOIN
	lojas l ON l.ID_Loja=p.ID_Loja
INNER JOIN
	clientes c ON c.ID_Cliente=p.ID_Cliente'''

# Para ler o banco com a query
df = pd.read_sql(query, conectar_banco)

# Movendo o conteudo para um arquivo CSV
df.to_csv("resumo_vendas.csv", index=False)

# Desativando a conexão
cursor.close()
conectar_banco.close()



