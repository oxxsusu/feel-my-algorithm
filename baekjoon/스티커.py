# 9465
T = int(input())

for _ in range(T):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]

    for y in range(1, n):
        if y==1:
            sticker[0][y] += sticker[1][y-1]
            sticker[1][y] += sticker[0][y-1]
        else:
            sticker[0][y] += max(sticker[1][y-1], max(sticker[0][y-2], sticker[1][y-2]))
            sticker[1][y] += max(sticker[0][y-1], max(sticker[0][y-2], sticker[1][y-2]))
    print(max(sticker[0][n-1], sticker[1][n-1]))