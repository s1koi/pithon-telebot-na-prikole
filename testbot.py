from random import choice # pyright: ignore[reportShadowedImports]
import config
import telebot
API_TOKEN = config.token

bot = telebot.TeleBot(API_TOKEN)
car = None

class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
    
    def info(self):
        return f"Информация о машине:\n\nЦвет: {self.color}\nМарка: {self.brand}"


@bot.message_handler(commands=['car'])
def car_com(message):
        global car
        textm = message.text.split()
        if len(textm) < 3:
            bot.reply_to(message, "что-то пошло не так :(")
            return
        
        color = textm[1]
        brand = ' '.join(textm[2:]) 
        car = Car(color, brand)
        car_info = car.info()
        bot.send_message(message.chat.id, car_info)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = """
    Приветствую!
    
    Для создания машины команда:
    /car цвет марка
    пример:
    /car красный Toyota Camry
    """
    bot.send_message(message.chat.id, welcome_text)

@bot.message_handler(commands=['info'])
def car_info(message):
    global car
    
    if car is None:
        bot.reply_to(message, "машина не создана, быстрее создай ее!")
    else:
        car_info = car.info()
        bot.send_message(message.chat.id, car_info)

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """
    Команды:
    /info - информация о машине
    /start - начать работу с ботом
    /car цвет марка - создать машину с указанными параметрами
    /help - вызвать это сообщение
    /coin - бросить монетку
    
    """
    bot.send_message(message.chat.id, help_text)
@bot.message_handler(commands=['coin'])
def coin_handler(message):
    coin = choice(["ОРЕЛ", "РЕШКА"])
    bot.reply_to(message, coin)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text) 

bot.infinity_polling()
