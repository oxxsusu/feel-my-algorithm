import heapq

n = int(input())
q = []

for _ in range(n):
    temp = list(map(int, input().split()))
    if temp[0] == 0:
        if len(q) == 0:
            print(-1)
        else:
            print(-heapq.heappop(q))
    else:
        for i in range(1, len(temp)):
            heapq.heappush(q, -temp[i])