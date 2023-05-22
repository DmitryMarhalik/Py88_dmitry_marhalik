import psycopg2

connection = psycopg2.connect(user="dm", database="energy_values", host="127.0.0.1", port="5432", password="113019")
input_values = input("Enter name_product, protein, fat , carbohydrate, kcal and gram separated by a space: ")
cursor = connection.cursor()
product_name, protein, fat, carbohydrate, kcal, *gram = input_values.split()
if gram:
    postgres_insert_query = """INSERT INTO product (name,protein,fat,carbohydrate,kcal,gram)
    VALUES (%s,%s,%s,%s,%s,%s)"""
    cursor.execute(postgres_insert_query, (product_name, protein, fat, carbohydrate, kcal, int(gram[0])))
    connection.commit()
else:
    postgres_insert_query = """INSERT INTO product (name,protein,fat,carbohydrate,kcal)
    VALUES (%s,%s,%s,%s,%s)"""
    cursor.execute(postgres_insert_query, (product_name, protein, fat, carbohydrate, kcal))
    connection.commit()

cursor.execute("SELECT * from product")
print("Результат", cursor.fetchall())
