import mysql.connector


# conexao = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='rootpassword',
#     database='bdyoutube',
# )

# cursor = conexao.cursor()


# cursor.close()
# conexao.close()

# CRUD

with mysql.connector.connect(
    host='localhost',
    user='root',
    password='rootpassword',
    database='bdyoutube',
) as conexao:
    with conexao.cursor() as cursor:
        nome = "amendoim"
        valor = 6
        comando = f'INSERT INTO Vendas (nome_produto, valor) VALUES ("{nome}", {valor})'
        cursor.execute(comando)
        conexao.commit() # edita o banco de dados
        # resultado = cursor.fetchall() ler o banco de dados e pegar as informações
         
# CREATE
# nome_produto = "chocolate"
# valor = 15
# comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados


# READ
# comando = f'SELECT * FROM vendas'
# cursor.execute(comando)
# resultado = cursor.fetchall() # ler o banco de dados
# print(resultado)


# UPDATE
# nome_produto = "todynho"
# valor = 6
# comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados

# DELETE
# nome_produto = "todynho"
# comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados
