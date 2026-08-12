
def solve1(n, b):
        
    b.sort(reverse=True)

    S = b[0]

    for i in range(1, n + 2):
        listaResposta.append(S - b[i])

    M = b.index(listaResposta[-1])


    M = listaResposta.pop(M - 1)


    print(f"{S} {listaResposta[-1]}")
    for resp in listaResposta:
        print(resp, end=" ")
    print()

listaResposta = []

n = int(input())

b = list(map(int, input().split()))

# pego o S
maior = -1
for i in range(n + 2):
    if maior < b[i]:
        maior = b[i]
b.remove(maior)

# faço as subtrações e somo tudo
conjugado = b.copy()
soma = 0
for i in range(n + 1):
    conjugado[i] = maior - b[i]
    soma += conjugado[i]
respM = soma - maior

M = b[conjugado.index(respM)]

conjugado.remove(respM)

conjugado.sort(reverse=False)

# resposta final
print(f"{maior} {M}")
print(" ".join(map(str, conjugado)))