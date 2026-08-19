from socket import *
from cesar import *
from diffie_hellman import *

serverName = "10.1.70.18"

serverPort = 12500
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))


dados = clientSocket.recv(1024).decode("utf-8")

p, g = map(int, dados.split(","))

if not eh_primo(p):
    print("Erro: p não é primo.")
    clientSocket.close()
    exit()

# segredo privado de Alice
a = 6

# chave pública de Alice
A = gerar_chave_publica(g, a, p)

# envia A para Bob
clientSocket.send(
    str(A).encode("utf-8")
)

# recebe B
B = int(
    clientSocket.recv(1024).decode("utf-8")
)

# calcula chave compartilhada
chave_compartilhada = gerar_chave_compartilhada(
    B,
    a,
    p
)

print("\n===== DIFFIE-HELLMAN =====")
print("p:", p)
print("g:", g)
print("Chave privada de Alice:", a)
print("Chave pública de Alice:", A)
print("Chave pública de Bob:", B)
print("Chave compartilhada:", chave_compartilhada)
sentence = input("Input lowercase sentence: ")
clientSocket.send(bytes(criptografar(sentence,3), "utf-8"))
modifiedSentence = clientSocket.recv(65000)
text = str(modifiedSentence,"utf-8")

print ("Received from Make Upper Case Server: ", descriptografar(text, 3))
clientSocket.close()

