a = input()
b = input()
x, y = len(a), len(b)
cache = [[0] * (y + 1) for _ in range(x + 1)]

for i in range(1, x+1):
    for j in range(1, y+1):
        if a[i-1] == b[j-1]:    # 글자 같은 경우 전 값에 +1
            cache[i][j] = cache[i-1][j-1]+1
        else:   # 다른 경우 직전 값 중 큰 것으로
            cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])

print(cache[x][y])