import mysql.connector

connection = mysql.connector.connect(
    host="localhost", user="root", password="root", database="bdyoutube"
)

cursor = connection.cursor()

# CREATE
product = "Toddynho"
value = 3

create_value = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{product}", {value})'
# cursor.execute(create_value)
# connection.commit()

# READ
search_value = 'SELECT * FROM vendas'
# cursor.execute(search_value)
# result = cursor.fetchall()
# print(result)

# UPDATE
update_value = f'UPDATE vendas SET valor = 6 WHERE id_vendas = 2'
# cursor.execute(update_value)
# connection.commit()

# DELETE
delete_item = f'DELETE FROM vendas WHERE id_vendas = 3'
cursor.execute(delete_item)
connection.commit()

# COMMANDS TO CLOSE CONNECTION
cursor.close()
connection.close()
