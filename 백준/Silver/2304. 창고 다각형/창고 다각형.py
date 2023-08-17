N = int(input())
garage = []
for _ in range(N):
    l, h = map(int, input().split())
    garage.append((l, h))

garage.sort(key=lambda x: x[0])
max_l, max_h = max(garage, key=lambda x: x[1])  # 높이 기준
max_idx = garage.index((max_l, max_h))
left, right = garage[:max_idx+1], list(reversed(garage[max_idx:]))

def polygon(r): # 범위 지정한 리스트
    ans = 0
    prev_h = r[0][1]
    for i in range(1, len(r)):
        w = abs(r[i][0] - r[i-1][0])
        ans += w * prev_h
        if prev_h < r[i][1]:
            prev_h = r[i][1]
    return ans

if N == 1:
    print(garage[0][1])
else:
    print(polygon(left)+max_h+polygon(right))