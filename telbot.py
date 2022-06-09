import telebot
from telebot import types
from telebot.types import KeyboardButton, ReplyKeyboardMarkup
import random
import requests
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('chave')

b = telebot.TeleBot(token)

# api da caixa https://github.com/guto-alves/loterias-api
apicaixa = 'https://loteriascaixa-api.herokuapp.com/api/mega-sena/latest'








bini = types.KeyboardButton('/start')
b1 = KeyboardButton('fazer jogo')
b6 = KeyboardButton('6')
b7 = KeyboardButton('7')
b8 = KeyboardButton('8')
b9 = KeyboardButton('9')
b10 = KeyboardButton('10')
b11 = KeyboardButton('11')
b12 = KeyboardButton('12')
b13 = KeyboardButton('13')
b14 = KeyboardButton('14')
b15 = KeyboardButton('15')
bur = KeyboardButton('último resultado')
bp = KeyboardButton('pesquise concurso')
ba = KeyboardButton('ajuda')
binfo = KeyboardButton('Info')
k1 = ReplyKeyboardMarkup(resize_keyboard=True)
k1.row(b1)
k1.row(bur, bp)
k1.row(ba, binfo, bini)
k2 = types.ForceReply(selective=False)
k3 = ReplyKeyboardMarkup(resize_keyboard=True)
k3.row(b6, b7, b8)
k3.row(b9, b10, b11)
k3.row(b12, b13, b14)
k3.row(b15)



@b.message_handler(commands=['start'])
def resp1(menss):
    b.reply_to(menss,
               "Bem vindo ao MegaSena BR Bot !!!!\nEscolha uma das opções abaixo ↓↓↓",
               reply_markup=k1)



@b.message_handler(commands=['stop'])
def resp2(menss):
    b.reply_to(menss, 'Valeus, Até a próxima')
    b.stop_bot()


@b.message_handler()
def botoes(menss):
    if menss.text == 'Info':
        b.reply_to(menss, '''\nMegaSenaBRbot v8.2\n
        ~~~~ >>> desenvolvido por github.com/zittox/\n\n
        ~~~ >>> GOSTOU? ajude a manter este projeto, copie a chave abaixo e contribua com pix\n
        fb337fa0-a417-4e25-bb23-4cd4c468b820\n\n
        Boa sorte na jogatina\n\n  :":": └[∵┌] └[ ∵ ]┘ [┐∵]┘ :":": \n\n ''', disable_web_page_preview=True)
        b.send_message(menss.chat.id,'Quer tentar mais alguma opção?\ncontinue nos botões abaixo ↓↓↓ ', reply_markup=k1)
    elif menss.text == 'ajuda':
        b.send_message(menss.chat.id, 'Para fazer um novo jogo ou pesquisar resultados, clique nos botões abaixo ↓↓↓')
    elif menss.text == 'último resultado':
        b.reply_to(menss, ultimo_resultado())
    elif menss.text == 'pesquise concurso':
        sentm = b.send_message(menss.chat.id, "Digite o número do concurso", reply_markup=k2)
        b.register_next_step_handler(sentm, concurso)
    elif menss.text == 'fazer jogo':
        sentm = b.send_message(menss.chat.id, 'Selecione quantos números tem seu jogo nos botões abaixo', reply_markup=k3)
        b.register_next_step_handler(sentm, faz_jogo)





def faz_jogo(menss):
    if menss.text == '6':
        j = random.sample(range(1, 61), 6)
        j.sort()
        jogox2 = ""
        while j:
            jogox2 = " - ".join(str(i) for i in j)
            break
        b.reply_to(menss, f'Seu jogo é:  {jogox2}\n\n Quer tentar mais alguma opção?\ncontinue nos botões abaixo ↓↓↓ ', reply_markup=k1)
    elif menss.text == '7':
        j = random.sample(range(1, 61), 7)
        j.sort()
        jogox2 = ""
        while j:
            jogox2 = " - ".join(str(i) for i in j)
            break
        b.reply_to(menss, f'Seu jogo é:  {jogox2}\n\n Quer tentar mais alguma opção?\ncontinue nos botões abaixo ↓↓↓ ', reply_markup=k1)
    elif menss.text == '8':
        j = random.sample(range(1, 61), 8)
        j.sort()
        jogox2 = ""
        while j:
            jogox2 = " - ".join(str(i) for i in j)
            break
        b.reply_to(menss, f'Seu jogo é:  {jogox2}\n\n Quer tentar mais alguma opção?\ncontinue nos botões abaixo ↓↓↓ ', reply_markup=k1)
    elif menss.text == '9':
        j = random.sample(range(1, 61), 9)
        j.sort()
        jogox2 = ""
        while j:
            jogox2 = " - ".join(str(i) for i in j)
            break
        b.reply_to(menss, f'Seu jogo é:  {jogox2}\n\n Quer tentar mais alguma opção?\ncontinue nos botões abaixo ↓↓↓ ', reply_markup=k1)
    elif menss.text == '10':
        j = random.sample(range(1, 61), 10)
        j.sort()
        jogox2 = ""
        while j:
            jogox2 = " - ".join(str(i) for i in j)
            break
        b.reply_to(menss, f'Seu jogo é:  {jogox2}\n\n Quer tentar mais alguma opção?\ncontinue nos botões abaixo ↓↓↓ ', reply_markup=k1)
    elif menss.text == '11':
        j = random.sample(range(1, 61), 11)
        j.sort()
        jogox2 = ""
        while j:
            jogox2 = " - ".join(str(i) for i in j)
            break
        b.reply_to(menss, f'Seu jogo é:  {jogox2}\n\n Quer tentar mais alguma opção?\ncontinue nos botões abaixo ↓↓↓ ', reply_markup=k1)
    elif menss.text == '12':
        j = random.sample(range(1, 61), 12)
        j.sort()
        jogox2 = ""
        while j:
            jogox2 = " - ".join(str(i) for i in j)
            break
        b.reply_to(menss, f'Seu jogo é:  {jogox2}\n\n Quer tentar mais alguma opção?\ncontinue nos botões abaixo ↓↓↓ ', reply_markup=k1)
    elif menss.text == '13':
        j = random.sample(range(1, 61), 13)
        j.sort()
        jogox2 = ""
        while j:
            jogox2 = " - ".join(str(i) for i in j)
            break
        b.reply_to(menss, f'Seu jogo é:  {jogox2}\n\n Quer tentar mais alguma opção?\ncontinue nos botões abaixo ↓↓↓ ', reply_markup=k1)
    elif menss.text == '14':
        j = random.sample(range(1, 61), 14)
        j.sort()
        jogox2 = ""
        while j:
            jogox2 = " - ".join(str(i) for i in j)
            break
        b.reply_to(menss, f'Seu jogo é:  {jogox2}\n\n Quer tentar mais alguma opção?\ncontinue nos botões abaixo ↓↓↓ ', reply_markup=k1)
    elif menss.text == '15':
        j = random.sample(range(1, 61), 15)
        j.sort()
        jogox2 = ""
        while j:
            jogox2 = " - ".join(str(i) for i in j)
            break
        b.reply_to(menss, f'Seu jogo é:  {jogox2}\n\n Quer tentar mais alguma opção?\ncontinue nos botões abaixo ↓↓↓ ', reply_markup=k1)



def concurso(menss):
    conc = menss.text
    apicaixaconc = f'https://loterias-caixa-gov.herokuapp.com/api/mega-sena/{conc}'
    if conc.isdecimal():
        try:
            r = requests.get(apicaixaconc).json()
            data = f"concurso: {r['concurso']}"
            data1 = f"Data: {r['data']}"
            data2 = "Dezenas: {} - {} - {} - {} - {} - {}".format(r['dezenas'][0], r['dezenas'][1], r['dezenas'][2],
                                                                  r['dezenas'][3], r['dezenas'][4], r['dezenas'][5])
            if r['premiacoes'] == [] or r['premiacoes'][0]['vencedores'] == 0:
                venc = f"Vencedores: Não"
            else:
                d = [[estado["uf"], estado["vencedores"]] for estado in r["estadosPremiados"]]
                estados = '  '.join(f'{estado[0]} - {estado[1]}' for estado in d)
                if len(d) == 1:
                    venc = f"Vencedor: {r['premiacoes'][0]['vencedores']}\nEstado:  {estados}\nPremiação: R$ {r['premiacoes'][0]['premio']}"
                else:
                    venc = f"Vencedores: {r['premiacoes'][0]['vencedores']}\nEstados:  {estados}\nPremiação: R$ {r['premiacoes'][0]['premio']}"
            quin = f"Quina: {r['premiacoes'][1]['vencedores']} - R$ {r['premiacoes'][1]['premio']}"
            quad = f"Quadra: {r['premiacoes'][2]['vencedores']} - R$ {r['premiacoes'][2]['premio']}"
            if r['acumulou'] == True:
                data3 = "Acumulou: Sim"
            else:
                data3 = "Acumulou: Não"
            data4 = f"Prox_prêmio: {r['acumuladaProxConcurso']}"
            data5 = f"Prox_concurso: {r['dataProxConcurso']}"
            b.reply_to(menss,
                       f'{data}\n{data1}\n{data2}\n{venc}\n{quin}\n{quad}\n{data3}\n{data4}\n{data5}\n\n Quer tentar mais alguma opção?\ncontinue nos botões abaixo ↓↓↓ ', reply_markup=k1)
        except ValueError:
            b.reply_to(menss, 'Esse número de concurso não exite,\naperte o botão -> pesquise concurso <-\n para tentar novamente', reply_markup=k1)
    else:
        b.reply_to(menss, 'Você não digitou número,\naperte o botão -> pesquise concurso <-\n para tentar novamente', reply_markup=k1)


def ultimo_resultado():
    apicaixa = 'https://loterias-caixa-gov.herokuapp.com/api/mega-sena/latest'
    r = requests.get(apicaixa).json()
    data = f"concurso: {r['concurso']}"
    data1 = f"Data: {r['data']}"
    data2 = "Dezenas: {} - {} - {} - {} - {} - {}".format(r['dezenas'][0], r['dezenas'][1], r['dezenas'][2],
                                                          r['dezenas'][3], r['dezenas'][4], r['dezenas'][5])
    if r['premiacoes'] == [] or r['premiacoes'][0]['vencedores'] == 0:
        venc = f"Vencedores: Não"
    else:
        d = [[estado["uf"], estado["vencedores"]] for estado in r["estadosPremiados"]]
        estados = '  '.join(f'{estado[0]} - {estado[1]}' for estado in d)
        if len(d) == 1:
            venc = f"Vencedor: {r['premiacoes'][0]['vencedores']}\nEstado:  {estados}\nPremiação: R$ {r['premiacoes'][0]['premio']}"
        else:
            venc = f"Vencedores: {r['premiacoes'][0]['vencedores']}\nEstados:  {estados}\nPremiação: R$ {r['premiacoes'][0]['premio']}"
    quin = f"Quina: {r['premiacoes'][1]['vencedores']} - R$ {r['premiacoes'][1]['premio']}"
    quad = f"Quadra: {r['premiacoes'][2]['vencedores']} - R$ {r['premiacoes'][2]['premio']}"
    if r['acumulou'] == True:
        data3 = "Acumulou: Sim"
    else:
        data3 = "Acumulou: Não"
    data4 = f"Prox_prêmio: {r['acumuladaProxConcurso']}"
    data5 = f"Prox_concurso: {r['dataProxConcurso']}"
    return f'{data}\n{data1}\n{data2}\n{venc}\n{quin}\n{quad}\n{data3}\n{data4}\n{data5}\n\n Quer tentar mais alguma opção?\ncontinue nos botões abaixo ↓↓↓ '



@b.message_handler(content_types=['photo'])
def foto(menss):
    b.send_message(menss.chat.id, 'bela foto')




b.infinity_polling()

