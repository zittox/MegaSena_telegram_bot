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



bini = types.KeyboardButton('/start')
k2 = types.ForceReply(selective=False)
#megasena
b1 = KeyboardButton('fazer jogo - MegaSena')
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
bur = KeyboardButton('último resultado\nMegaSena')
bp = KeyboardButton('pesquise concurso\nMegaSena')
ba = KeyboardButton('ajuda')
binfo = KeyboardButton('Info')
k1 = ReplyKeyboardMarkup(resize_keyboard=True)
k1.row(b1)
k1.row(bur, bp)
k1.row(ba, binfo, bini)
k3 = ReplyKeyboardMarkup(resize_keyboard=True)
k3.row(b6, b7, b8)
k3.row(b9, b10, b11)
k3.row(b12, b13, b14)
k3.row(b15)
#lotofacil
l1 = KeyboardButton('15')
l2 = KeyboardButton('16')
l3 = KeyboardButton('17')
l4 = KeyboardButton('18')
k4 = ReplyKeyboardMarkup(resize_keyboard=True)
k4.row(l1, l2)
k4.row(l3, l4)
b1a = KeyboardButton('fazer jogo - Lotofácil')
urlf = KeyboardButton('último resultado\nLotofácil')
prlf = KeyboardButton('pesquise concurso\nLotofácil')
k6 = ReplyKeyboardMarkup(resize_keyboard=True)
k6.row(b1a)
k6.row(urlf, prlf)
k6.row(ba, binfo, bini)

#menu principal
k5 = ReplyKeyboardMarkup(resize_keyboard=True)
mp1 = KeyboardButton('/MegaSena')
mp2 = KeyboardButton('/Lotofácil')
k5.row(mp1, mp2)
k5.row(ba, binfo, bini)



@b.message_handler(commands=['start'])
def resp1(menss):
    b.reply_to(menss,
               "Bem vindo ao MegaSena+ BR Bot !!!!\nEscolha uma das opções abaixo ↓↓↓",
               reply_markup=k5)

@b.message_handler(commands=['Lotofácil'])
def resplotofacil(menss):
    b.send_message(menss.chat.id, 'Escolha uma das opções abaixo ↓↓↓\n ou aperte o /start para recomeçar e escolher outra loteria', reply_markup=k6)


@b.message_handler(commands=['MegaSena'])
def botoes(menss):
    b.send_message(menss.chat.id, 'Escolha uma das opções abaixo ↓↓↓\n ou aperte o /start para recomeçar e escolher outra loteria', reply_markup=k1)






@b.message_handler()
def botoes(menss):
    if menss.text == 'Info':
        b.reply_to(menss, '''\n\nMegaSenaBRbot+ v2.1 - Agora também com Lotofácil\n
        ~~~~ >>> desenvolvido por github.com/zittox/\n\n
        ~~~ >>> GOSTOU? ajude a manter este projeto, copie a chave abaixo e contribua com pix\n
        fb337fa0-a417-4e25-bb23-4cd4c468b820\n\n
        Boa sorte na jogatina\n\n  :":": └[∵┌] └[ ∵ ]┘ [┐∵]┘ :":": \n\n ''', disable_web_page_preview=True)
        b.send_message(menss.chat.id,'Quer tentar mais alguma opção?\ncontinue nos botões abaixo ↓↓↓\n ou aperte o /start para recomeçar e escolher outra loteria', reply_markup=k5)
    elif menss.text == 'ajuda':
        b.send_message(menss.chat.id, 'Para fazer um novo jogo ou pesquisar resultados, clique nos botões abaixo ↓↓↓\n ou aperte o /start para recomeçar e escolher outra loteria', reply_markup=k5)
    elif menss.text == 'último resultado\nLotofácil':
        b.reply_to(menss, ultimo_resultado_lotofacil())
    elif menss.text == 'pesquise concurso\nLotofácil':
        sentm = b.send_message(menss.chat.id, "Digite o número do concurso", reply_markup=k2)
        b.register_next_step_handler(sentm, concurso_lotofacil)
    elif menss.text == 'fazer jogo - Lotofácil':
        sentm = b.send_message(menss.chat.id, 'Selecione quantos números tem seu jogo nos botões abaixo', reply_markup=k4)
        b.register_next_step_handler(sentm, faz_jogo_lotofacil)
    elif menss.text == 'último resultado\nMegaSena':
        b.reply_to(menss, ultimo_resultado())
    elif menss.text == 'pesquise concurso\nMegaSena':
        sentm = b.send_message(menss.chat.id, "Digite o número do concurso", reply_markup=k2)
        b.register_next_step_handler(sentm, concurso)
    elif menss.text == 'fazer jogo - MegaSena':
        sentm = b.send_message(menss.chat.id, 'Selecione quantos números tem seu jogo nos botões abaixo', reply_markup=k3)
        b.register_next_step_handler(sentm, faz_jogo)








#LOTOFACIL_________________________________________________________________________

def faz_jogo_lotofacil(menss):
    j = random.sample(range(1, 25), int(menss.text))
    j.sort()
    jogox2 = ""
    while j:
        jogox2 = " - ".join(str(i) for i in j)
        break
    b.reply_to(menss, f'Seu jogo é:  {jogox2}\n\n Quer tentar mais alguma opção?\ncontinue nos botões abaixo ↓↓↓\n ou aperte o /start para recomeçar e escolher outra loteria', reply_markup=k6)


def concurso_lotofacil(menss):
    conc = menss.text
    apicaixaconc = f'https://loterias-caixa-gov.herokuapp.com/api/lotofacil/{conc}'
    if conc.isdecimal():
        try:
            r = requests.get(apicaixaconc).json()
            data = f"concurso: {r['concurso']}"
            data1 = f"Data: {r['data']}"
            data2 = "Dezenas: {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}".format(r['dezenas'][0], r['dezenas'][1], r['dezenas'][2],
                                                                  r['dezenas'][3], r['dezenas'][4], r['dezenas'][5],
                                                                  r['dezenas'][6], r['dezenas'][7], r['dezenas'][8],
                                                                  r['dezenas'][9], r['dezenas'][10], r['dezenas'][11],
                                                                  r['dezenas'][12], r['dezenas'][13], r['dezenas'][14])
            if r['premiacoes'] == [] or r['premiacoes'][0]['vencedores'] == 0:
                venc = f"Vencedores: Não"
            else:
                d = [[estado["uf"], estado["vencedores"]] for estado in r["estadosPremiados"]]
                estados = '  '.join(f'{estado[0]} - {estado[1]}' for estado in d)
                if len(d) == 1:
                    venc = f"Vencedor: {r['premiacoes'][0]['vencedores']}\nEstado:  {estados}\nPremiação: R$ {r['premiacoes'][0]['premio']}"
                else:
                    venc = f"Vencedores: {r['premiacoes'][0]['vencedores']}\nEstados:  {estados}\nPremiação: R$ {r['premiacoes'][0]['premio']}"
            quatpnts = f"14 Pontos: {r['premiacoes'][1]['vencedores']} - R$ {r['premiacoes'][1]['premio']}"
            trezpnts = f"13 Pontos: {r['premiacoes'][2]['vencedores']} - R$ {r['premiacoes'][2]['premio']}"
            dozepnts = f"12 Pontos: {r['premiacoes'][3]['vencedores']} - R$ {r['premiacoes'][3]['premio']}"
            onezpnts = f"11 Pontos: {r['premiacoes'][4]['vencedores']} - R$ {r['premiacoes'][4]['premio']}"
            if r['acumulou'] == True:
                data3 = "Acumulou: Sim"
            else:
                data3 = "Acumulou: Não"
            data4 = f"Prox_prêmio: {r['acumuladaProxConcurso']}"
            data5 = f"Prox_concurso: {r['dataProxConcurso']}"
            b.reply_to(menss,
                       f'{data}\n\n{data1}\n\n{data2}\n\n{venc}\n\n{quatpnts}\n\n{trezpnts}\n\n{dozepnts}\n\n{onezpnts}\n\n{data3}\n\n{data4}\n\n{data5}\n\n Quer tentar mais alguma opção?\ncontinue nos botões abaixo ↓↓↓\n ou aperte o /start para recomeçar e escolher outra loteria', reply_markup=k6)
        except ValueError:
            b.reply_to(menss, 'Esse número de concurso não exite,\naperte o botão -> pesquise concurso <-\n para tentar novamente', reply_markup=k6)
    else:
        b.reply_to(menss, 'Você não digitou número,\naperte o botão -> pesquise concurso <-\n para tentar novamente', reply_markup=k6)

def ultimo_resultado_lotofacil():
    apicaixa = 'https://loterias-caixa-gov.herokuapp.com/api/lotofacil/latest'
    r = requests.get(apicaixa).json()
    try:
        data = f"concurso: {r['concurso']}"
        data1 = f"Data: {r['data']}"
        data2 = "Dezenas: {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}".format(r['dezenas'][0], r['dezenas'][1], r['dezenas'][2],
                                                              r['dezenas'][3], r['dezenas'][4], r['dezenas'][5],
                                                              r['dezenas'][6], r['dezenas'][7], r['dezenas'][8],
                                                              r['dezenas'][9], r['dezenas'][10], r['dezenas'][11],
                                                              r['dezenas'][12], r['dezenas'][13], r['dezenas'][14])
        if r['premiacoes'] == [] or r['premiacoes'][0]['vencedores'] == 0:
            venc = f"Vencedores: Não"
        else:
            d = [[estado["uf"], estado["vencedores"]] for estado in r["estadosPremiados"]]
            estados = '  '.join(f'{estado[0]} - {estado[1]}' for estado in d)
            if len(d) == 1:
                venc = f"Vencedor: {r['premiacoes'][0]['vencedores']}\nEstado:  {estados}\nPremiação: R$ {r['premiacoes'][0]['premio']}"
            else:
                venc = f"Vencedores: {r['premiacoes'][0]['vencedores']}\nEstados:  {estados}\nPremiação: R$ {r['premiacoes'][0]['premio']}"
        quatpnts = f"14 Pontos: {r['premiacoes'][1]['vencedores']} - R$ {r['premiacoes'][1]['premio']}"
        trezpnts = f"13 Pontos: {r['premiacoes'][2]['vencedores']} - R$ {r['premiacoes'][2]['premio']}"
        dozepnts = f"12 Pontos: {r['premiacoes'][3]['vencedores']} - R$ {r['premiacoes'][3]['premio']}"
        onezpnts = f"11 Pontos: {r['premiacoes'][4]['vencedores']} - R$ {r['premiacoes'][4]['premio']}"
        if r['acumulou'] == True:
            data3 = "Acumulou: Sim"
        else:
            data3 = "Acumulou: Não"
        data4 = f"Prox_prêmio: {r['acumuladaProxConcurso']}"
        data5 = f"Prox_concurso: {r['dataProxConcurso']}"
        return f'{data}\n\n{data1}\n\n{data2}\n\n{venc}\n\n{quatpnts}\n\n{trezpnts}\n\n{dozepnts}\n\n{onezpnts}\n\n{data3}\n\n{data4}\n\n{data5}\n\n Quer tentar mais alguma opção?\ncontinue nos botões abaixo ↓↓↓ \n ou aperte o /start para recomeçar e escolher outra loteria'
    except IndexError:
        return f'Aguardando atualização dos resultados para o último concurso\nfavor tentar novamente mais tarde\n'


#LOTOFACIL_________________________________________________________________________








#megasena _________________________________________________________________________

def faz_jogo(menss):

    j = random.sample(range(1, 61), int(menss.text))
    j.sort()
    jogox2 = ""
    while j:
        jogox2 = " - ".join(str(i) for i in j)
        break
    b.reply_to(menss, f'Seu jogo é:  {jogox2}\n\n Quer tentar mais alguma opção?\ncontinue nos botões abaixo ↓↓↓\n ou aperte o /start para recomeçar e escolher outra loteria', reply_markup=k1)


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
                       f'{data}\n\n{data1}\n\n{data2}\n\n{venc}\n\n{quin}\n\n{quad}\n\n{data3}\n\n{data4}\n\n{data5}\n\n Quer tentar mais alguma opção?\ncontinue nos botões abaixo ↓↓↓\n ou aperte o /start para recomeçar e escolher outra loteria', reply_markup=k1)

        except ValueError:
            b.reply_to(menss, 'Esse número de concurso não exite,\naperte o botão -> pesquise concurso <-\n para tentar novamente', reply_markup=k1)
    else:
        b.reply_to(menss, 'Você não digitou número,\naperte o botão -> pesquise concurso <-\n para tentar novamente', reply_markup=k1)


def ultimo_resultado():
    apicaixa = 'https://loterias-caixa-gov.herokuapp.com/api/mega-sena/latest'
    r = requests.get(apicaixa).json()
    try:
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

        return f'{data}\n\n{data1}\n\n{data2}\n\n{venc}\n\n{quin}\n\n{quad}\n\n{data3}\n\n{data4}\n\n{data5}\n\n Quer tentar mais alguma opção?\ncontinue nos botões abaixo ↓↓↓ \n ou aperte o /start para recomeçar e escolher outra loteria'
    except IndexError:
        return f'Aguardando atualização dos resultados para o último concurso\nfavor tentar novamente mais tarde\n'
#megasena _________________________________________________________________________





b.infinity_polling()

