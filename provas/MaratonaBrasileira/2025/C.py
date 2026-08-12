

n = int(input())

a = list(map(str, input().split()))
resp = 0

while len(a) != 1:
    if a[-1] == "0":
        a.pop()

    else:
        novo = ["1"]
        aux = a.copy()
        aux.append("0")


        length = len(aux)
        for i in range(1, len(a)):
            if a[i] == aux[i - 1]:
                novo.append("0")

            else:
                novo.append("1")
        novo.append("0")
        a = novo

    resp += 1


print(resp)