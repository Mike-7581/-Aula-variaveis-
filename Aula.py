nome = "Talysson Aguinário Grande Dos Santos"
idade = 16
a = 22
b = 13
cidade = "Canápolis"
x = 7
y = 3
pi = 3.14159
mensagem = "Eu tomei no cu "
base = 12176
altura = 16
area = (base * altura)
saldo = 1000
subtrair_saldo = (1000 - 250)
primeiro_nome = "Talysson"
Sobrenome = "Grande"
nome_completo = (primeiro_nome + Sobrenome)

while True:
    pergunta = input("Qual variável? ")

    if pergunta == "nome":
        print(nome)
    elif pergunta == "idade":
        print(idade)
    elif pergunta == "a":
        print(a)
    elif pergunta == "b":
        print(b)
    elif pergunta == "cidade":
        print("Eu moro em", cidade)
    elif pergunta == "x":
        print(x - y)
    elif pergunta == "mensagem":
        print(mensagem * 3)
    elif pergunta == "area":
        print(area)
    elif pergunta == "saldo":
        print(saldo)
    elif pergunta == "subtrair saldo":
        print(subtrair_saldo)
    elif pergunta == "pi":
        print(pi)
    elif pergunta == "nome completo":
        print(nome_completo)


    else:
        print("Error!")
