

n = int(input())



# topo
print(f"{chr(32)*n}{chr(95)*(n+1)}")

# parte superior

for i in range(n, 1, -1):
    print(f"{chr(32)*(i - 1)}{chr(47)}{chr(32)*(n+1 + (n- i)*2)}{chr(92)}")

# meio
print(f"{chr(47)}{chr(95)*n}{chr(32)*(2*(n - 1)+1)}{chr(92)}{chr(95)*(n+1)}")


# parte inferior
for i in range(1, n):
    print(f"{chr(32)*(n + i)}{chr(92)}{chr(32)*(n+1 + (n- i)*2)}{chr(47)}")


# fim
print(f"{chr(32)*(2*n)}{chr(92)}{chr(95)*(n+1)}{chr(47)}")

