
def resp(p, r):

    if p == 0:
        return "C"
    
    if r == 0:
        return "B"
    
    return "A"

p, r = map(int, input().split())

print(resp(p, r))