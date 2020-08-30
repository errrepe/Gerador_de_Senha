def gera_senha():
    import random

    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz' # 26 caracteres
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # 26 caracteres
    digits = '0123456789'# 10 caracteres
    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""" # 32 caracteres

    numero_de_caracteres = 6
    i = 0
    senha_gerada = ""
    while i < numero_de_caracteres:
        seed = random.randint(0,100)
        if seed % 2:
            seed2 = random.randint(0, len(ascii_lowercase)-1)
            senha_gerada += ascii_lowercase[seed2]
        elif seed % 3:
            seed2 = random.randint(0, len(ascii_uppercase)-1)
            senha_gerada += ascii_uppercase[seed2]
        elif seed % 5:
            seed2 = random.randint(0, len(digits)-1)
            senha_gerada += digits[seed2]
        elif seed % 7:
            seed2 = random.randint(0, len(punctuation)-1)
            senha_gerada += punctuation[seed2]
        i += 1
    return senha_gerada




print(gera_senha())