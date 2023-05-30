from itertools import combinations

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def func(selection):
    cd = 0
    for hx, hy in house:
        _min = float('inf')
        for sx, sy in selection:
            d = abs(sx-hx) + abs(sy-hy)
            if d < _min:
                _min = d
        cd += _min

    return cd

house, chicken = [], []
for x in range(n):
    for y in range(n):
        if city[x][y] == 1:
            house.append((x, y))
        if city[x][y] == 2:
            chicken.append((x, y))

selections = combinations(chicken, m)
ans = float('inf')
for selection in selections:
    cd = func(selection)
    if cd < ans:
        ans = cd

print(ans)