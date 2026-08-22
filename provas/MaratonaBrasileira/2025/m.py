

def d(x):
    print(f"{x}")
def solve(x, n, k):

    lo, hi = 1, max(x) + k + 1
    ans = 0

    def menor_muro(t):

        conjuntoI = 0
        conjuntoF = n - 1
        for i in range(n):


            if t > x[i]:
                if t - x[i] > k:
                    return False

                atualI = i
                atualF = min(n - 1, k - (t - x[i]) + i) 


                conjuntoI = max(conjuntoI, atualI)
                conjuntoF = min(conjuntoF, atualF)




            if conjuntoF < conjuntoI:
                return False
        return True

        

    while lo <= hi:
        mid = (lo + hi) // 2
        if menor_muro(mid):
            ans = mid
            lo = mid + 1

        else:
            hi = mid - 1

    return ans

n, k = map(int, input().split())
x = list(map(int, input().split()))


print(solve(x, n, k))