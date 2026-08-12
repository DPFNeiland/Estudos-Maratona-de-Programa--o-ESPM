
d = list(map(int, input().split()))

resp = 4

for i in range(1, 5):
    if i in d:
        resp -=1


print(resp)
