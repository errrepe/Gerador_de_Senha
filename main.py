# TODO: Evitar caracteres repetidos
# TODO: Numero minimo de dígitos


def pergunta_usuario():
    resp = input('Digite [S] para sim e [N] para não\n').upper()
    if resp == 'S':
        return True
    if resp == 'N':
        return False
    elif resp != 'N' or resp != 'S':
        print('Por favor digite apenas [S] ou [N]')
        pergunta_usuario()


def gera_senha():
    import random

    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz' # 26 caracteres
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # 26 caracteres
    digits = '0123456789'# 10 caracteres
    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""" # 32 caracteres

    numero_de_caracteres = int(input('Digite o número de caracteres que a senha deve ter: '))
    if type(numero_de_caracteres) is not int:
        print('Por favor digite apenas um numero.')
        gera_senha()

    print('A senha deverá ter caracteres especiais?')
    resp_caracteres_especiais = pergunta_usuario()
    if resp_caracteres_especiais == True:
        min_caracteres_especiais = int(input('Numero minimo de caracteres especiais: '))
        if min_caracteres_especiais > numero_de_caracteres:
            print('O numero de caracteres especiais não pode ser maior que o número de caracteres totais')
            gera_senha()


    # print('A senha pode ter caracteres repetidos??')
    # resp_caracteres_repetidos = pergunta_usuario()

    i = 0
    senha_gerada = ""
    contador_carac_especiais = 0


    while i < numero_de_caracteres:
        seed = random.randint(0,100)
        if seed % 2 and seed <=50:
            seed2 = random.randint(0, len(ascii_lowercase)-1)
            senha_gerada += ascii_lowercase[seed2]
        elif seed % 3:
            seed2 = random.randint(0, len(ascii_uppercase)-1)
            senha_gerada += ascii_uppercase[seed2]
        elif seed % 5 and seed >= 50:
            seed2 = random.randint(0, len(digits)-1)
            senha_gerada += digits[seed2]
        elif seed % 7 and resp_caracteres_especiais == True:
            seed2 = random.randint(0, len(punctuation)-1)
            senha_gerada += punctuation[seed2]
        i += 1

        if i == numero_de_caracteres:
            for n in range(0, len(senha_gerada)):
                if senha_gerada[n] in punctuation:
                    contador_carac_especiais += 1
            if contador_carac_especiais < min_caracteres_especiais:
                i = 0
                senha_gerada = ""
                contador_carac_especiais = 0


    return senha_gerada




print(gera_senha())

