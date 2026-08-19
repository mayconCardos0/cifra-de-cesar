from socket import *

from cesar import criptografar, descriptografar

from diffie_hellman import (
    eh_primo,
    gerar_chave_publica,
    gerar_chave_compartilhada
)

serverPort = 12500

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(("", serverPort))

serverSocket.listen(5)

print("TCP Server\n")

connectionSocket, addr = serverSocket.accept()

p = 23
g = 5
b = 7


if not eh_primo(p):
    print("Erro: p não é primo.")
    connectionSocket.close()
    serverSocket.close()
    exit()

# Envia parâmetros públicos
connectionSocket.send(
    f"{p},{g}".encode("utf-8")
)

# Recebe A de Alice
A = int(
    connectionSocket.recv(1024).decode("utf-8")
)

# Calcula B
B = gerar_chave_publica(g, b, p)


# Calcula chave compartilhada
chave_compartilhada = gerar_chave_compartilhada(
    A,
    b,
    p
)


# Envia B para Alice
connectionSocket.send(
    str(B).encode("utf-8")
)


print("\n===== DIFFIE-HELLMAN =====")
print("p:", p)
print("g:", g)
print("Chave privada de Bob:", b)
print("Chave pública de Alice:", A)
print("Chave pública de Bob:", B)
print("Chave compartilhada:", chave_compartilhada)

sentence = connectionSocket.recv(65000)

sentence = sentence.decode("utf-8")

print("Received From Client: ", descriptografar(sentence, 3))

capitalizedSentence = sentence.upper()

connectionSocket.send(capitalizedSentence.encode("utf-8"))

print("Sent back to Client: ", capitalizedSentence)

connectionSocket.close()