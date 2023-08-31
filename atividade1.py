def soma(N):
    if N <= 0:
        return 0
    else:
        return N + soma(N - 1)


n = 50
resultado = soma(n)
print(f"A soma dos primeiros {n} números inteiros positivos é {resultado}.")
