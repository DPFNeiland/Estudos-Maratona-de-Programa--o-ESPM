

listaResposta = []

n = int(input())

b = list(map(int, input().split()))

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