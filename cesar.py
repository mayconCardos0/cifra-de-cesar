def criptografar(texto, chave):
    resultado = ""

    chave = chave % 26

    for caractere in texto:

        if 'A' <= caractere <= 'Z':
            novo_caractere = chr(
                (ord(caractere) - ord('A') + chave) % 26
                + ord('A')
            )
            resultado += novo_caractere

        elif 'a' <= caractere <= 'z':
            novo_caractere = chr(
                (ord(caractere) - ord('a') + chave) % 26
                + ord('a')
            )
            resultado += novo_caractere

        else:
            resultado += caractere

    return resultado


def descriptografar(texto, chave):
    return criptografar(texto, -chave)