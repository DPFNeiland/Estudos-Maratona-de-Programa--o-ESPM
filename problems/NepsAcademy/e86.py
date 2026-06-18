
def resp(a, b):
    
    if a + b >= 14:
        return "Aprovado"

    if a + b < 8:
        return "Reprovado"
    
    return "Recuperacao"





A, B = map(float, input().split())

print(resp(A, B))