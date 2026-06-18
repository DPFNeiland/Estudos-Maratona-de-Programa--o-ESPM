

n = int(input())
resps = []


# 1° a gente inverte o eixo y
# 2° vê se ele aplica nessas inequações:
# a) y <= x + 200
# b) y <= 100
# c) y <= -x + 100

for i in range(n):
    x, y = map(int, input().split())

    if y < 0:
        x *= -1 
        y *= -1 

    if (y <= x + 200) and (y <= 100) and (y <= -x + 100):
        resps.append("S")
    else:
        resps.append("N")

for resposta in resps:
    print(resposta)