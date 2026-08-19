# Comunicação TCP com Cifra de César e Diffie-Hellman

Este projeto implementa uma comunicação entre um **cliente e um servidor TCP utilizando Python**.

O objetivo é demonstrar conceitos fundamentais de **Sistemas Distribuídos**, **comunicação através de sockets**, **criptografia de mensagens** e **troca de chaves criptográficas**.

A aplicação utiliza:

* **Sockets TCP** para a comunicação entre cliente e servidor;
* **Cifra de César** para criptografar e descriptografar mensagens;
* **Algoritmo Diffie-Hellman** para realizar a troca de uma chave compartilhada;
* **Teste de números primos** para validar o parâmetro utilizado no Diffie-Hellman.

## Estrutura do projeto

```text
cifra-de-cesar/
│
├── cesar.py
├── client.py
├── server.py
├── diffie_hellman.py
│
└── docs/
```

### `cesar.py`

Responsável pela implementação da **Cifra de César**.

O arquivo possui duas funções principais:

* `criptografar(texto, chave)`
* `descriptografar(texto, chave)`

A implementação suporta letras maiúsculas e minúsculas, preservando espaços, números e caracteres especiais.

Exemplo:

```text
Texto original: HELLO
Chave: 3

Texto criptografado: KHOOR
```

A descriptografia é realizada aplicando o deslocamento negativo da chave.

---

### `diffie_hellman.py`

Implementa as funções utilizadas durante a troca de chaves pelo algoritmo **Diffie-Hellman**.

Principais funções:

```python
eh_primo(n)
```

Verifica se um número é primo.

```python
gerar_chave_publica(g, segredo_privado, p)
```

Gera uma chave pública utilizando:

```text
chave_publica = g^segredo_privado mod p
```

```python
gerar_chave_compartilhada(chave_publica, segredo_privado, p)
```

Calcula a chave compartilhada:

```text
chave_compartilhada = chave_publica^segredo_privado mod p
```

---

### `server.py`

Implementa o servidor TCP.

O servidor:

1. Cria um socket TCP;
2. Aguarda a conexão de um cliente;
3. Define os parâmetros públicos `p` e `g` do Diffie-Hellman;
4. Envia os parâmetros públicos ao cliente;
5. Recebe a chave pública do cliente;
6. Calcula e envia sua própria chave pública;
7. Calcula a chave compartilhada;
8. Recebe uma mensagem criptografada utilizando a Cifra de César;
9. Descriptografa a mensagem para exibição;
10. Converte a mensagem para maiúsculas;
11. Envia a resposta ao cliente.

---

### `client.py`

Implementa o cliente TCP.

O cliente:

1. Conecta-se ao servidor;
2. Recebe os parâmetros públicos do Diffie-Hellman;
3. Valida se o número `p` é primo;
4. Gera sua chave pública;
5. Envia sua chave pública ao servidor;
6. Recebe a chave pública do servidor;
7. Calcula a chave compartilhada;
8. Solicita uma mensagem ao usuário;
9. Criptografa a mensagem utilizando a Cifra de César;
10. Envia a mensagem criptografada ao servidor;
11. Recebe a resposta e realiza a descriptografia.

## Funcionamento do Diffie-Hellman

O projeto utiliza os seguintes parâmetros:

```text
p = 23
g = 5
```

Cada participante possui um segredo privado.

### Cliente — Alice

```text
a = 6
```

A chave pública é calculada como:

```text
A = g^a mod p
```

### Servidor — Bob

```text
b = 7
```

A chave pública é calculada como:

```text
B = g^b mod p
```

Após a troca das chaves públicas, ambos calculam a mesma chave compartilhada.

Cliente:

```text
K = B^a mod p
```

Servidor:

```text
K = A^b mod p
```

Dessa forma:

```text
K_cliente = K_servidor
```

A chave privada de cada participante não é transmitida pela rede.

## Fluxo da comunicação

O funcionamento da aplicação pode ser representado da seguinte forma:

```text
CLIENTE                                  SERVIDOR
   │                                         │
   │──────── Conexão TCP ────────────────────▶│
   │                                         │
   │◀─────── p, g ───────────────────────────│
   │                                         │
   │──────── Chave pública A ───────────────▶│
   │                                         │
   │◀─────── Chave pública B ────────────────│
   │                                         │
   │   Calcula chave compartilhada           │
   │                                         │
   │──────── Mensagem criptografada ────────▶│
   │                                         │
   │                         Descriptografa a mensagem
   │                                         │
   │◀─────── Mensagem em maiúsculas ─────────│
   │                                         │
   │ Descriptografa a resposta               │
   │                                         │
```

## Tecnologias utilizadas

* Python 3
* Socket TCP/IP
* Cifra de César
* Diffie-Hellman

Não são utilizadas bibliotecas externas.

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/mayconCardos0/cifra-de-cesar.git
```

Entre na pasta do projeto:

```bash
cd cifra-de-cesar
```

### 2. Configure o endereço do servidor

No arquivo `client.py`, configure a variável:

```python
serverName = "IP_DO_SERVIDOR"
```

Caso cliente e servidor estejam na mesma máquina, utilize:

```python
serverName = "127.0.0.1"
```

Caso estejam em máquinas diferentes, utilize o endereço IP da máquina onde o servidor está sendo executado.

### 3. Inicie o servidor

```bash
python server.py
```

O servidor ficará aguardando uma conexão TCP na porta:

```text
12500
```

### 4. Inicie o cliente

Em outro terminal ou computador:

```bash
python client.py
```

O cliente realizará a conexão, executará a troca de chaves Diffie-Hellman e solicitará uma mensagem.

Exemplo:

```text
Input lowercase sentence: ola mundo
```

A mensagem será criptografada antes de ser transmitida.

O servidor receberá a mensagem criptografada, realizará a descriptografia para exibição, converterá o conteúdo para maiúsculas e enviará a resposta ao cliente.

## Observação

A implementação da **Cifra de César** e os valores utilizados no **Diffie-Hellman** possuem finalidade **didática**.

A Cifra de César não oferece segurança adequada para aplicações reais, e os parâmetros utilizados no Diffie-Hellman são pequenos e utilizados apenas para facilitar a compreensão e os testes do algoritmo.

Em aplicações reais, devem ser utilizados algoritmos criptográficos modernos e bibliotecas especializadas para garantir a segurança da comunicação.

Projeto desenvolvido para fins acadêmicos, com o objetivo de aplicar conceitos de **Sistemas Distribuídos**, **Sockets TCP**, **Criptografia** e **Troca de Chaves**.
