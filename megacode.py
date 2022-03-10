
import time
import qrandom


class Mega:
    quantinum = int()
    numjog = int()

    def __init__(self, numjog, quantinum):
        self.numjog = numjog
        self.quantinum = quantinum

    @classmethod
    def mostra_jogo(cls):
        jogo2 = [qrandom.sample(range(1, 61), cls.quantinum) for i in range(cls.numjog)]

        while jogo2:
            for i in jogo2:
                i.sort()
            break
        jogo2.sort()

        jogox2 = ""
        while jogo2:
            for i in jogo2:
                i.sort()
                time.sleep(1)
                jogox2 = "\n".join(str(i) for i in jogo2)
            break


        if cls.numjog == 1:
            print(f'O jogo de {cls.quantinum} números é :\n{jogox2}')
            cls.pergunta_sim_nao("Gostaria de continuar?")
        else:
            print(f'Os {cls.numjog} jogos de {cls.quantinum} números são:\n')
            time.sleep(2)
            print(f'{jogox2}\n')
            cls.pergunta_sim_nao("Gostaria de continuar?")

    @classmethod
    def perg1(cls):
        while True:
            cls.quantinum = input(
                "\nQuantos números tem o jogo da MEGA SENA que você quer?\ndigite uma opção: 6, 7, 8 ou 9\n")
            try:
                cls.quantinum = int(cls.quantinum)
                if cls.quantinum == 6 or cls.quantinum == 7 or cls.quantinum == 8 or cls.quantinum == 9:
                    print(f"\n~~~~>> Você escolheu ter {cls.quantinum} números em cada jogo ----~!~~!~~!\n")
                    break
                elif cls.quantinum != range(6, 10):
                    print("\n!!!!! >>>> Escolha um número entre 6 e 9 <<<< !!!")
                    cls.perg1()
            except ValueError:
                print("\n!!!!! >>>> PRESTENÇÃO: escolha um número <<<< !!!!")
                cls.perg1()
            return cls.quantinum

    @classmethod
    def perg2(cls):

        while True:
            cls.numjog = input(f"Quantos jogos você gostaria de ter com {cls.quantinum} números?\n")
            try:
                cls.numjog = int(cls.numjog)
                if cls.numjog == 0:
                    print("\n!!!!! >>>> ZERO jogadas não é um número válido neh, tenta de novo! <<<< !!!!\n")
                    cls.perg2()
                if cls.numjog > 100:
                    print("\nO máximo são 100 jogadas <<<--------\n")
                    cls.perg2()
                elif cls.numjog >= 1 and cls.numjog <= 100:
                    print(f"\n~~~~>> Você escolheu {cls.numjog} jogos\n\nCALCULAND0 ~~~~ └[∵┌]└[ ∵ ]┘[┐∵]┘\n")
                break
            except ValueError:
                print("\n!!!!! >>>> PRESTENÇÃO: digite um número entre 1 e 100 <<<< !!!!\n")
                cls.perg2()

            return cls.numjog

    @classmethod
    def pergunta_sim_nao(cls, menssagem):

        resposta = ""
        while resposta not in ("s", "n"):
            resposta = input(f"\n{menssagem} (s ou n): ")
            if resposta not in ("s", "n"):
                print("\nPor favor, digite sim \"s\" ou não \"n\"")
            elif resposta == "n":
                print("\n__ Boa sorte!\n >>>>> Até a próxima!!!")
                break
            else:
                cls.perg1()
                cls.perg2()
                cls.mostra_jogo()


Mega.pergunta_sim_nao(" ~~~~~~ Bem vindo ____\nGostaria de fazer jogo(s) da Mega Sena?")
