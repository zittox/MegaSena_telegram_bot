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
# bpara = types.KeyboardButton('/stop')
b6 = KeyboardButton('6')
b7 = KeyboardButton('7')
b8 = KeyboardButton('8')
b9 = KeyboardButton('9')
bur = KeyboardButton('último resultado')
bp = KeyboardButton('pesquise concurso')
ba = KeyboardButton('ajuda')
binfo = KeyboardButton('Info')
k1 = ReplyKeyboardMarkup(resize_keyboard=True)
k1.row(b6, b7, b8, b9)
k1.row(bur, bp)
k1.row(ba, binfo, bini)
k2 = types.ForceReply(selective=False)


@b.message_handler(commands=['start'])
def resp1(menss):
    b.reply_to(menss,
               "Bem vindo ao gerador de jogo(s) da Mega Sena!!!!\nPara fazer um jogo de 6, 7 , 8 ou 9 números: clique nos números\nOu escolha uma das outras opções abaixo ↓↓↓",
               reply_markup=k1)


# será q quando tiver hosteado na nuvem ele volta funcionar com /strat?
@b.message_handler(commands=['stop'])
def resp2(menss):
    b.reply_to(menss, 'Valeus, Até a próxima')
    b.stop_bot()


@b.message_handler()
def botoes(menss):
    if menss.text == 'Info':
        b.reply_to(menss, '''\nMegaSenaBRbot v7.3\n
        ~~~~ >>> desenvolvido por github.com/zittox/\n\n
        ~~~ >>> GOSTOU? ajude a manter este projeto, copie a chave abaixo e contribua com pix\n
        fb337fa0-a417-4e25-bb23-4cd4c468b820\n\n
        Boa sorte na jogatina\n\n  :":": └[∵┌] └[ ∵ ]┘ [┐∵]┘ :":": \n\n ''')
    elif menss.text == '6':
        j = random.sample(range(1, 61), 6)
        j.sort()
        jogox2 = ""
        while j:
            jogox2 = " - ".join(str(i) for i in j)
            break
        b.reply_to(menss, f'Seu jogo é:  {jogox2}\n\n Quer tentar mais alguma opção?\ncontinue nos botões abaixo ↓↓↓ ')
    elif menss.text == '7':
        j = random.sample(range(1, 61), 7)
        j.sort()
        jogox2 = ""
        while j:
            jogox2 = " - ".join(str(i) for i in j)
            break
        b.reply_to(menss, f'Seu jogo é:  {jogox2}\n\n Quer tentar mais alguma opção?\ncontinue nos botões abaixo ↓↓↓ ')
    elif menss.text == '8':
        j = random.sample(range(1, 61), 8)
        j.sort()
        jogox2 = ""
        while j:
            jogox2 = " - ".join(str(i) for i in j)
            break
        b.reply_to(menss, f'Seu jogo é:  {jogox2}\n\n Quer tentar mais alguma opção?\ncontinue nos botões abaixo ↓↓↓ ')
    elif menss.text == '9':
        j = random.sample(range(1, 61), 9)
        j.sort()
        jogox2 = ""
        while j:
            jogox2 = " - ".join(str(i) for i in j)
            break
        b.reply_to(menss, f'Seu jogo é:  {jogox2}\n\n Quer tentar mais alguma opção?\ncontinue nos botões abaixo ↓↓↓ ')
    elif menss.text == 'ajuda':
        b.send_message(menss.chat.id, 'Para fazer um novo jogo ou pesquisar resultados, clique nos botões abaixo ↓↓↓')
    elif menss.text == 'último resultado':
        b.reply_to(menss, ultimo_resultado())
    elif menss.text == 'pesquise concurso':
        sentm = b.send_message(menss.chat.id, "Digite o número do concurso", reply_markup=k2)
        b.register_next_step_handler(sentm, concurso)


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
                venc = "Vencedores: {} - {}".format(r['premiacoes'][0]['vencedores'], str(d))
            if r['premiacoes'] == [] or r['premiacoes'][0]['premio'] == "-":
                prem = f"Premiações: 0"
            else:
                prem = f"Premiações: R$ {r['premiacoes'][0]['premio']}"
            if r['acumulou'] == True:
                data3 = "Acumulou: Sim"
            else:
                data3 = "Acumulou: Não"
            data4 = f"Prox_prêmio: {r['acumuladaProxConcurso']}"
            data5 = f"Prox_concurso: {r['dataProxConcurso']}"
            b.reply_to(menss,
                       f'{data}\n{data1}\n{data2}\n{venc}\n{prem}\n{data3}\n{data4}\n{data5}\n\n Quer tentar mais alguma opção?\ncontinue nos botões abaixo ↓↓↓ ', reply_markup=k1)
        except ValueError:
            b.reply_to(menss, 'Esse número de concurso não exite,\naperte o botão -> pesquise concurso <-\n para tentar novamente', reply_markup=k1)
    else:
        b.reply_to(menss, 'Você não digitou número,\naperte o botão -> pesquise concurso <-\n para tentar novamente', reply_markup=k1)


def ultimo_resultado():
    apicaixa = 'https://loterias-caixa-gov.herokuapp.com/api/mega-sena/latest'
    r = requests.get(apicaixa).json()
    data = f"{r['concurso']}"
    data1 = f"Data: {r['data']}"
    data2 = "Dezenas: {} - {} - {} - {} - {} - {}".format(r['dezenas'][0], r['dezenas'][1], r['dezenas'][2],
                                                          r['dezenas'][3], r['dezenas'][4], r['dezenas'][5])
    if r['premiacoes'] == [] or r['premiacoes'][0]['vencedores'] == 0:
        venc = f"Vencedores: Não"
    else:
        d = [[estado["uf"], estado["vencedores"]] for estado in r["estadosPremiados"]]
        venc = f"Vencedores: {r['premiacoes'][0]['vencedores']} - {d}"
    if r['premiacoes'] == [] or r['premiacoes'][0]['premio'] == "-":
        prem = f"Premiações: 0"
    else:
        prem = f"Premiações: R$ {r['premiacoes'][0]['premio']}"
    if r['acumulou'] == True:
        data3 = "Acumulou: Sim"
    else:
        data3 = "Acumulou: Não"
    data4 = f"Prox_prêmio: {r['acumuladaProxConcurso']}"
    data5 = f"Prox_concurso: {r['dataProxConcurso']}"
    return f'{data}\n{data1}\n{data2}\n{venc}\n{prem}\n{data3}\n{data4}\n{data5}\n\n Quer tentar mais alguma opção?\ncontinue nos botões abaixo ↓↓↓ '



@b.message_handler(content_types=['photo'])
def foto(menss):
    b.send_message(menss.chat.id, 'bela foto')


# @b.message_handler(content_types=['input'])
# def qqtexto(menss):
# b.reply_to(menss, 'Para fazer um novo jogo ou pesquisar resultados, clique nos botões abaixo')


b.infinity_polling()
