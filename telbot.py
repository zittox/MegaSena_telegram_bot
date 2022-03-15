import telebot
from telebot import types
import time
import qrandom
import requests


# api da caixa https://github.com/guto-alves/loterias-api
apicaixa = 'https://loteriascaixa-api.herokuapp.com/api/mega-sena/latest'

def ultimo_resultado():
    r = requests.get(apicaixa).json()
    data = f" concurso: {r['concurso']}\ndata: {r['data']}\ndezenas: {r['dezenas']}\nacumulou: {r['acumulou']}\nprox_premio: {r['acumuladaProxConcurso']}\nprox_concurso: {r['dataProxConcurso']}"
    return data


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
    nur = types.KeyboardButton('/último_resultado')
    naj = types.KeyboardButton('/ajuda')
    markup.add(n6,n7,n8,n9,nur,naj)
    b.reply_to(menss, "\n Bem vindo ao gerador de jogo(s) da Mega Sena\n Este bot somente funciona com os botões na própria tela\nQuantos números tem o jogo da MEGA SENA que você quer fazer?", reply_markup=markup)

@b.message_handler(commands=["último_resultado"])
def nur(menss):
    b.reply_to(menss, ultimo_resultado())

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
def n7(menss):
    j = qrandom.sample(range(1, 61), 7)
    j.sort()
    jogox2 = ""
    while j:
        for i in j:
            jogox2 = " - ".join(str(i) for i in j)
        break
    b.reply_to(menss, f'Seu jogo é:  {jogox2}')

@b.message_handler(commands=["8_números"])
def n8(menss):
    j = qrandom.sample(range(1, 61), 8)
    j.sort()
    jogox2 = ""
    while j:
        for i in j:
            jogox2 = " - ".join(str(i) for i in j)
        break
    b.reply_to(menss, f'Seu jogo é:  {jogox2}')

@b.message_handler(commands=["9_números"])
def n9(menss):
    j = qrandom.sample(range(1, 61), 9)
    j.sort()
    jogox2 = ""
    while j:
        for i in j:
            jogox2 = " - ".join(str(i) for i in j)
        break
    b.reply_to(menss, f'Seu jogo é:  {jogox2}')

@b.message_handler(content_types=['ajuda','text'])
def texto(menss):
    b.send_message(menss.chat.id, 'Para fazer um novo jogo clique nos botões')

@b.message_handler(content_types=['photo'])
def foto(menss):
    b.send_message(menss.chat.id, 'bela foto')




b.polling()