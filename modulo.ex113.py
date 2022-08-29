def leiaint(n):
    while True:
        try:
            num = int(input(n))
        except (ValueError, TypeError):
            print("\033[1;31mERRO! INFORME UM VALOR INTEIRO\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[1;31mO USUÁRIO DECIDIU PARAR O PROGRAMA\033[m")
            return f'\033[7;31;40mNão foi informado nenhum valor\033[m'
        else:   #se tudo der certo, retorne o número informado
            return f'\033[1;36m{num}\033[m'

def leiafloat(numero):
    while True:
        try:
            variavel=float(input(numero))
        except (ValueError,TypeError):
            print("\033[1;31mERRO! INFORME UM VALOR REAL\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[1;31mO USUÁRIO DECIDIU PARAR O PROGRAMA\033[m")
            return f'\033[7;31;40mNão foi informado nenhum valor\033[m'
        else:
            return f'\033[1;36m{variavel}\033[m'
