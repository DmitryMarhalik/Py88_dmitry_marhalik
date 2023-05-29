import json
import psycopg2
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return """ 
    <form method="POST">
        <head>
            <title>Start page</title>
        </head>
        <div class="container">
           <button type="button"><a href="/add_product">Enter product</a></button></br>         
           <button type="button"><a href="/give_json">Give json</a></button>          
        </div>
    </form>         
    """


@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        product = request.form.get('Product')
        proteins = request.form.get('Proteins')
        fats = request.form.get('Fats')
        carbohydrates = request.form.get('Carbohydrates')
        Kcal = request.form.get('Kcal')
        connection = psycopg2.connect(user="dm", database="energy_values", host="127.0.0.1", port="5432",
                                      password="113019")
        cursor_db = connection.cursor()
        postgres_insert_query = """INSERT INTO product (name,protein,fat,carbohydrate,kcal)
                                   VALUES (%s,%s,%s,%s,%s)"""
        cursor_db.execute(postgres_insert_query, (product, proteins, fats, carbohydrates, Kcal))
        connection.commit()
        connection.close()
        return """
              <h1>Product added successfully!</h1>
               """
    else:
        return """
           <form method="POST">
            <head>
               <title>Enter product page</title>
            </head>
             <div class="container" align="center">
              <label for="Product"><b>Product</b></label>
              <input type="text" name="Product"><br>
              <label for="Proteins"><b>Proteins</b></label>
              <input type="Proteins" name="Proteins"><br>
              <label for="Fats"><b>Fats</b></label>
              <input type="Fats" name="Fats"><br>
              <label for="Carbohydrates"><b>Carbohydrates</b></label>
              <input type="Carbohydrates" name="Carbohydrates"><br>
              <label for="Kcal"><b>Kcal</b></label>                  
              <input type="Kcal" name="Kcal"><br>
              <button type="submit"c>Accept </button>
              <h4><a href='/'><= back</a></h4>
             </div>
           </form>
           """


@app.route('/give_json', methods=['GET'])
def give_json():
    if request.method == 'GET':
        connection = psycopg2.connect(user="dm", database="energy_values", host="127.0.0.1", port="5432",
                                      password="113019")
        cursor = connection.cursor()
        postgres_insert_query = """SELECT*FROM product"""
        cursor.execute(postgres_insert_query)
        connection.commit()
        prod_db = cursor.fetchall()
        connection.close()
        with open("db.json", "r") as my_json_file:
            db = json.load(my_json_file)
        for row in prod_db:
            db.append({"Id": row[0],
                       "Product": row[1],
                       "proteins": row[2],
                       "fats": row[3],
                       "carbohydrate": row[4],
                       "Kcal": row[5]})
        return db
        # return f"""
        # <form method="POST">
        #     <head>
        #        <title>Give JSON</title>
        #     </head>
        #     {db}
        #     <h4><a href='/'><= back</a></h4>
        # </form>"""


if __name__ == "__main__":
    app.run()
