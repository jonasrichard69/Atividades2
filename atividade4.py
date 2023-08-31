def decimalforbi(numero):
    pilha = []

    while numero > 0:
        resto = numero % 2
        pilha.append(resto)
        numero //=2

    if not pilha:
        pilha.append (0)

    binario = ""
    while len(pilha)>0:
        binario += str(pilha.pop())

    return binario


numerodec = int(input("digite um numero decimal: "))
numerobi = decimalforbi(numerodec)
print(f"o numero decimal {numerodec} em binario é: {numerobi}")