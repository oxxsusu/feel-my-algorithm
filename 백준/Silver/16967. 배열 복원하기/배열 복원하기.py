h, w, x, y = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(h+x)]
a = [[0]*w for _ in range(h)]

# x,y부터 h-x줄 w-y칸 겹침
for r in range(h):
    for c in range(w):
        a[r][c] = b[r][c]

# 겹치기 시작
for r in range(x, h):
    for c in range(y, w):
        a[r][c] = b[r][c] - a[r-x][c-y]

# 출력
for r in range(h):
    print(*a[r])