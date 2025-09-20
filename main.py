import telebot 
from config import token
from time import sleep
from logic import Pokemon, Wizard, Fighter
from random import randint
feed = 0
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['go'])
def start(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        chance = randint(1,3)
        if chance == 1:
            pokemon = Pokemon(message.from_user.username)
        elif chance == 2:
            pokemon = Wizard(message.from_user.username)
        elif chance == 3:
            pokemon = Fighter(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")


@bot.message_handler(commands=['attack'])
def attack_pok(message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.username in Pokemon.pokemons.keys() and message.from_user.username in Pokemon.pokemons.keys():
            enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
            pok = Pokemon.pokemons[message.from_user.username]
            res = pok.attack(enemy)
            bot.send_message(message.chat.id, res)
        else:
            bot.send_message(message.chat.id, "Сражаться можно только с покемонами")
    else:
            bot.send_message(message.chat.id, "Чтобы атаковать, нужно ответить на сообщения того, кого хочешь атаковать") 
@bot.message_handler(commands=['reload'])
def reload(message):
    bot.reply_to(message, "Покемон пересоздан!")
    pokemon = Pokemon(message.from_user.username)  
    bot.send_message(message.chat.id, pokemon.info())
    bot.send_photo(message.chat.id, pokemon.show_img())

@bot.message_handler(commands=['feed'])
def feed(message):
    if feed == 0:
        bot.reply_to(message, "Ты покормил покемона")
        feed = 1
        sleep(100)
        print ("Покемон проголодался, покорми его!")
        feed1 = 0
    else:
        bot.reply_to(message, "Ты уже кормил покемона")

bot.infinity_polling(none_stop=True)

