import psycopg2
import telebot
from telebot import types

# token=os.environ.get("tkn")
connection = psycopg2.connect(user="dm", database="telegram_db_products",
                              host="127.0.0.1", port="5432", password="113019")
cursor = connection.cursor()
bot = telebot.TeleBot('6008131787:AAFkUFNPbdifwmuGD8QXsr-Tak8KlIh2xmA')



@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton("Register")
    button_2 = types.KeyboardButton("Enter product in database")
    button_3 = types.KeyboardButton('Enter intake')
    markup.add(button_1,button_2, button_3,row_width=1)
    # or markup.row(button_1)
    #    markup.row(button_2, button_3)
    bot.send_message(message.from_user.id, "Hello. Please, choice the operation", reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

@bot.message_handler()
def on_click(message):
    if message.text == "Register":
        try:
            postgres_insert_query = """INSERT INTO users (chat_id_telegram) VALUES (%s)"""
            cursor.execute(postgres_insert_query, (message.from_user.id,))
            connection.commit()
            tg_id = message.from_user.id
            bot.send_message(message.from_user.id, f"Registered successfull. Your telegram id -- {tg_id}")
        except psycopg2.errors.UniqueViolation:
            bot.send_message(message.from_user.id, "Id already exists")

    elif message.text == "Enter product in database":
        bot.send_message(message.from_user.id,
                         "Enter name_product, protein, fat , carbohydrate, kcal separated by a space: ")
        bot.register_next_step_handler(message, add_product)

    elif message.text == "Enter intake":
        bot.send_message(message.from_user.id,
                         "Enter your product_id and product quantity in grams by a space: ")
        bot.register_next_step_handler(message, intake)


def add_product(message):
    product_name, protein, fat, carbohydrate, kcal = message.text.split(" ")
    postgres_insert_query = """INSERT INTO products (name,proteins,fats,carbohydrates,kcal)
        VALUES (%s,%s,%s,%s,%s)"""
    cursor.execute(postgres_insert_query, (product_name, float(protein),
                                           float(fat), float(carbohydrate), float(kcal)))
    connection.commit()
    bot.send_message(message.from_uder.id, "The additional went well!")


def intake(message):
    product_id, gram = message.text.split(" ")
    postgres_insert_query1 = """select users.id from users where users.chat_id_telegram = %s"""
    # postgres_insert_query1 = f"""select users.id from users where users.chat_id_telegram =
    # {(str(message.from_user.id))}"""
    postgres_insert_query2 = """INSERT INTO intake (user_id, product_id, gram) VALUES (%s,%s,%s)"""

    cursor.execute(postgres_insert_query1, (message.from_user.id,))
    user_id = cursor.fetchone()[0]
    cursor.execute(postgres_insert_query2, (user_id, int(product_id), float(gram)))
    connection.commit()
    bot.send_message(message.from_user.id, "The intake added!")


bot.polling(none_stop=True)
