import sqlite3
#Criando o Banco de Dados:
#
conexao = sqlite3.connect('clientes.db')
#
# # Criando o cursor:
c = conexao.cursor()
#
# # Criando a tabela:
#
c.execute("""CREATE TABLE clientes (
nome text,
sobrenome text,
email text,
telefone text
)""")
#
# #Commit as mudanças:
conexao.commit()
#
# #Fechar o banco de dados:
conexao.close()