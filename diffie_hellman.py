def eh_primo(n):
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    i = 3

    while i * i <= n:
        if n % i == 0:
            return False

        i += 2

    return True

def gerar_chave_publica(g, segredo_privado, p):
    return pow(g, segredo_privado, p)


def gerar_chave_compartilhada(chave_publica, segredo_privado, p):
    return pow(chave_publica, segredo_privado, p)