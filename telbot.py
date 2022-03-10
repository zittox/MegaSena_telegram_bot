import telebot
from telebot import types
import time
import qrandom

with open("chave.txt", "r") as c:
    chave = c.read()

b = telebot.TeleBot(chave)



@b.message_handler(commands=['start'])
def resp1(menss):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    n6 = types.KeyboardButton('/6_números')
    n7 = types.KeyboardButton('/7_números')
    n8 = types.KeyboardButton('/8_números')
    n9 = types.KeyboardButton('/9_números')
    markup.add(n6,n7,n8,n9)
    b.reply_to(menss, "\n Bem vindo ao gerador de jogo(s) da Mega Sena\nQuantos números tem o jogo da MEGA SENA que você quer fazer?", reply_markup=markup)


@b.message_handler(commands=["6_números"])
def n6(menss):
    j = qrandom.sample(range(1, 61), 6)
    j.sort()
    jogox2 = ""
    while j:
        for i in j:
            jogox2 = " - ".join(str(i) for i in j)
        break
    b.reply_to(menss, f'Seu jogo é:  {jogox2}')

@b.message_handler(commands=["7_números"])
def n6(menss):
    j = qrandom.sample(range(1, 61), 7)
    j.sort()
    jogox2 = ""
    while j:
        for i in j:
            jogox2 = " - ".join(str(i) for i in j)
        break
    b.reply_to(menss, f'Seu jogo é:  {jogox2}')

@b.message_handler(commands=["8_números"])
def n6(menss):
    j = qrandom.sample(range(1, 61), 8)
    j.sort()
    jogox2 = ""
    while j:
        for i in j:
            jogox2 = " - ".join(str(i) for i in j)
        break
    b.reply_to(menss, f'Seu jogo é:  {jogox2}')

@b.message_handler(commands=["9_números"])
def n6(menss):
    j = qrandom.sample(range(1, 61), 9)
    j.sort()
    jogox2 = ""
    while j:
        for i in j:
            jogox2 = " - ".join(str(i) for i in j)
        break
    b.reply_to(menss, f'Seu jogo é:  {jogox2}')


b.polling()