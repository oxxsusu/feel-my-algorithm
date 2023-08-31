N = int(input())
cp = [tuple(map(int, input().split())) for _ in range(N)]
ans, memo = float('inf'), [0]

def taxi_distance(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

# 전체
for j in range(1, N):
    memo.append(taxi_distance(cp[j-1], cp[j]))

total = sum(memo)
for i in range(1, N-1):     # i번째를 건너뛴 거리 중 최소값 구하기
    temp = total - (memo[i]+memo[i+1]) + taxi_distance(cp[i-1], cp[i+1])
    ans = min(ans, temp)

print(ans)