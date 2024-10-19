import telebot
import numpy as np
from telebot import types

# Укажите токен вашего бота, полученный от @BotFather
API_TOKEN = '7922958927:AAGjqjhkWj09SknESN8O_bO3s0OtCTPYEqE'

bot = telebot.TeleBot(API_TOKEN)

# Основное меню при команде /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Решить математическую задачу")
    btn2 = types.KeyboardButton("Совет по продвижению компании")
    btn3 = types.KeyboardButton("Новая компания")
    btn4 = types.KeyboardButton("О компании")
    btn5 = types.KeyboardButton("Контакты")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, "Привет! Я ваш ИИ-помощник. Чем могу помочь?", reply_markup=markup)

# Обработка кнопки "Решить математическую задачу"
@bot.message_handler(func=lambda message: message.text == "Решить математическую задачу")
def math_task(message):
    bot.send_message(message.chat.id, "Введите математическое выражение (например: 2 + 2 или sqrt(16)).")

# Обработка математического выражения
@bot.message_handler(func=lambda message: any(op in message.text for op in ['+', '-', '*', '/', 'sqrt', '^']))
def solve_math(message):
    try:
        expression = message.text.replace('^', '**').replace('sqrt', 'np.sqrt')
        result = eval(expression)
        bot.send_message(message.chat.id, f"Ответ: {result}")
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка: {str(e)}")

# Обработка кнопки "Совет по продвижению компании"
@bot.message_handler(func=lambda message: message.text == "Совет по продвижению компании")
def marketing_tip(message):
    tips = [
        "Создайте качественный сайт с описанием ваших услуг.",
        "Используйте социальные сети для продвижения своего бренда.",
        "Создайте контент, который будет полезен вашей целевой аудитории.",
        "Проведите анализ конкурентов и найдите их слабые стороны.",
        "Используйте SEO для повышения видимости вашего сайта в поисковых системах.",
        "Запустите рекламную кампанию с таргетингом на целевую аудиторию."
    ]
    bot.send_message(message.chat.id, np.random.choice(tips))

# Обработка кнопки "Новая компания"
@bot.message_handler(func=lambda message: message.text == "Новая компания")
def new_company(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Начать новую кампанию", callback_data='start_campaign')
    markup.add(btn1)
    bot.send_message(message.chat.id, "Вы хотите начать новую маркетинговую кампанию?", reply_markup=markup)

# Обработка кнопки "О компании"
@bot.message_handler(func=lambda message: message.text == "О компании")
def about_company(message):
    bot.send_message(message.chat.id, "Наша компания занимается маркетингом и продвижением бизнеса.")

# Обработка кнопки "Контакты"
@bot.message_handler(func=lambda message: message.text == "Контакты")
def contacts(message):
    bot.send_message(message.chat.id, "Связаться с нами можно по телефону: +7 (123) 456-78-90")

# Обработка нажатия на Inline-кнопки
@bot.callback_query_handler(func=lambda call: call.data == 'start_campaign')
def callback_inline(call):
    if call.message:
        bot.send_message(call.message.chat.id, "Маркетинговая кампания начата!")

# Запускаем бот
bot.polling()
