# 2407
def ft(v):
    while v > 1:
        result = v * ft(v-1)
        return result
    return 1

n, m = map(int, input().split())
print(ft(n) // (ft(m) * ft(n-m)))
