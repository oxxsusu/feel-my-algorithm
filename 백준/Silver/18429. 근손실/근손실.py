from itertools import permutations

n, k = map(int, input().split())
kit = list(map(int, input().split()))

p = permutations(kit, n)
ans = 0
for exercises in p:
    w = 500
    keep = True
    for exercise in exercises:
        w += exercise - k
        if w < 500: # 한번이라도 500 밑으로 떨어지면 out
            keep = False
            break
    if keep:
        ans += 1
        
print(ans)