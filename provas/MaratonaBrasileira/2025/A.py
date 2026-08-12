

n, m = list(map(int, input().split()))

resp = 0
g = []

for _ in range(n):
    aux = list(map(int, input().split())) 
    g.append(aux)


for i in range(m):
    maxAux = -1
    for j in range(n):
        if g[j][i] > maxAux:
            maxAux = g[j][i]

    resp += maxAux

print(resp)
