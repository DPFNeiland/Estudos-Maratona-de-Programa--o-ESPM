
def divisor(n):
    max = int(pow(n, 1/2)) + 1
    for i in range(3, max, 2):

        if n % i == 0:
            return i

def potencia_modular(base, expo, modulo):
    bolso = 1
    # bolso vazio
    base  = base % modulo
    while expo > 0:
        if expo % 2 == 1:   # ímpar
            bolso = (bolso * base) % modulo
        base = (base * base) % modulo  # Regra B
        expo = expo // 2
    return bolso

N, E, C = map(int, input().split())

p = divisor(N)
q = N//p

# função fi
fi = (p-1)*(q-1)
d = pow(E, -1, fi)

m = potencia_modular(C, d, N)

print(m)