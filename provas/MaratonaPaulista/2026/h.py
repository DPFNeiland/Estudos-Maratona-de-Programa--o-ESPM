


n = int(input())

t = list(map(int, input().split()))

resp = 0
horarioAtual = 60*5

for i in range(n):
    resp += t[i]    
    horarioAtual += t[i]

if horarioAtual > 7*60:
    resp += 3*60
    horarioAtual += 3*60

if horarioAtual > 17*60:
    resp += 3*60
    horarioAtual += 3*60

print(resp)