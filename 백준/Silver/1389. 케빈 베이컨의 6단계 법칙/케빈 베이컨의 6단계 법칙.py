from collections import deque

N, M = map(int, input().split())
adj = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)

cd = []
for i in range(N):
    count = 0
    visited = [False]*N
    visited[i] = True
    q = deque()
    q.append((i, 1))

    while q:
        v, k = q.popleft()
        for a in adj[v]:
            if not visited[a]:
                visited[a] = True
                count += k
                q.append((a, k+1))

    cd.append(count)

mc = min(cd)
print(cd.index(mc)+1)