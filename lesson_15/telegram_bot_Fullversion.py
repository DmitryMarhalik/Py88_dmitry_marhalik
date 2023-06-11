import os
import psycopg2
import telebot

from dotenv import load_dotenv
from telebot import types
from collections import Counter

load_dotenv()
connection = psycopg2.connect(user="dm", database="telegram_db_products",
                              host="127.0.0.1", port="5432", password=os.getenv("PASSWORD"))
cursor = connection.cursor()
bot = telebot.TeleBot(os.getenv("TOKEN"))


@bot.message_handler(commands=["start"])
def start(message):
    if check_id(message):
        markup = types.ReplyKeyboardMarkup()
        button_1 = types.KeyboardButton("View all id's of products")
        button_2 = types.KeyboardButton("Add a product")
        button_3 = types.KeyboardButton("Enter intake")
        button_4 = types.KeyboardButton("Calculation result")
        markup.add(button_1, button_2, button_3, button_4, row_width=1)
        bot.send_message(message.from_user.id, "Hello. Please, choice the operation", reply_markup=markup)
        bot.register_next_step_handler(message, on_click)
    else:
        button_1 = types.KeyboardButton("Register")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True).add(button_1)
        bot.send_message(message.from_user.id, "You are not registered. "
                                               "Please, click the 'Register' button", reply_markup=markup)
        bot.register_next_step_handler(message, on_click)


@bot.message_handler()
def on_click(message):
    if message.text == "Register":
        markup = types.ReplyKeyboardMarkup()
        postgres_insert_query = """INSERT INTO users (chat_id_telegram) VALUES (%s)"""
        cursor.execute(postgres_insert_query, (message.from_user.id,))
        connection.commit()
        telegram_id = message.from_user.id
        bot.send_message(message.from_user.id, f"Registered successfull. "
                                               f"Your telegram id -- {telegram_id}.", reply_markup=markup)
        start(message)
    elif message.text == "View all id's of products":
        postgres_insert_query = """select id,name from products order by name"""
        cursor.execute(postgres_insert_query, (message.from_user.id,))
        all_idproducts = cursor.fetchall()
        connection.commit()
        bot.send_message(message.from_user.id, "The database contains the following "
                                               "products and their id's")
        for product in all_idproducts:
            bot.send_message(message.from_user.id, f"{product[1]}--> "
                                                   f"id - {product[0]}")
    elif message.text == "Add a product":
        bot.send_message(message.from_user.id,
                         "Enter name_product, protein, fat , carbohydrate, kcal "
                         "per 100 grams separated by a space: ")
        bot.register_next_step_handler(message, add_product)
    elif message.text == "Enter intake":
        bot.send_message(message.from_user.id,
                         "Enter your product_id and product quantity in grams by a space: ")
        bot.register_next_step_handler(message, intake)
    elif message.text == "Calculation result":
        bot.send_message(message.from_user.id, "For what time period to calculate the result? "
                                               "Enter the number of days: ")
        bot.register_next_step_handler(message, finally_calculation)


def check_id(message):
    try:
        postgres_insert_query1 = """select users.id from users where users.chat_id_telegram = %s"""
        cursor.execute(postgres_insert_query1, (message.from_user.id,))
        user_id_in_data = cursor.fetchone()[0]
        return user_id_in_data
    except TypeError:
        return False


def add_product(message):
    try:
        product_name, protein, fat, carbohydrate, kcal = message.text.split(" ")
        postgres_insert_query = """INSERT INTO products (name,proteins,fats,carbohydrates,kcal)
            VALUES (%s,%s,%s,%s,%s)"""
        cursor.execute(postgres_insert_query, (product_name, float(protein),
                                               float(fat), float(carbohydrate), float(kcal)))
        connection.commit()
        bot.send_message(message.from_user.id, "Product added successfully!")
    except ValueError:
        bot.send_message(message.from_user.id, "Incorrect input product. Please, try again")


def intake(message):
    try:
        product_id, gram = message.text.split(" ")
        postgres_insert_query1 = """select users.id from users where users.chat_id_telegram = %s"""
        # or postgres_insert_query1 = f"""select users.id from users where users.chat_id_telegram =
        # {(str(message.from_user.id))}"""
        postgres_insert_query2 = """INSERT INTO intake (user_id, product_id, gram) VALUES (%s,%s,%s)"""
        cursor.execute(postgres_insert_query1, (message.from_user.id,))
        user_id = cursor.fetchone()[0]
        cursor.execute(postgres_insert_query2, (user_id, int(product_id), float(gram)))
        connection.commit()
        bot.send_message(message.from_user.id, "The intake added!")
    except ValueError:
        bot.send_message(message.from_user.id, "Incorrect input intake. Please, try again")


def calculation_all_idproducts(message):
    try:
        days = int(message.text)
        postgres_insert_query = f"""select product_id from intake where (time > now() - interval '%s days' 
          and user_id = {str(check_id(message))})"""
        cursor.execute(postgres_insert_query, (days,))
        return cursor.fetchall()
    except ValueError:
        return False


def finally_calculation(message):
    idproducts = calculation_all_idproducts(message)
    all_products, view_all_products, all_energy_values, \
        nice_count_of_product, view_all_products = [], [], [], [], []
    if idproducts != False and idproducts != []:
        for id in idproducts:
            postgres_insert_query = """select name from products where id=%s"""
            cursor.execute(postgres_insert_query, id)
            product = cursor.fetchone()
            all_products.append(product)

        for name in all_products:
            view_all_products.append(name[0])
            postgres_insert_query = """select proteins,fats,carbohydrates, kcal from products where name=%s"""
            cursor.execute(postgres_insert_query, name)
            energy_values = cursor.fetchone()
            all_energy_values.append(energy_values)

        all_proteins = all_fats = all_carbohydrates = all_kcal = 0
        for el in all_energy_values:
            all_proteins += el[0]
            all_fats += el[1]
            all_carbohydrates += el[2]
            all_kcal += el[3]
        count_of_product = Counter(view_all_products)

        for k, v in count_of_product.items():
            nice_count_of_product.append(f"{k}->{v} times\n")
        result_message = f"Нou have eaten the following foods:\n{''.join(nice_count_of_product)}\n" \
                         f"Total amount of protein:  {all_proteins} gr,\nfats: {all_fats} gr,\n" \
                         f"carbohydrates: {all_carbohydrates} gr,\nKcal: {all_kcal}"
        bot.send_message(message.from_user.id, result_message)

    elif idproducts == []:
        bot.send_message(message.from_user.id, "You haven't eaten anything during this time")
    else:
        bot.send_message(message.from_user.id, "Incorrect input days. Please, try again")


bot.polling(none_stop=True)
