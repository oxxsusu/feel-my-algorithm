n = int(input())
p, q = map(int, input().split())
m = int(input())
relation = [[] for _ in range(n+1)]
answer = [0]*(n+1)  # 촌수 저장용
for _ in range(m):
    parent, child = map(int, input().split())
    relation[parent].append(child)
    relation[child].append(parent)

visit = [False] * (n+1)
def dfs(v):
    visit[v] = True # 방문처리 먼저 하고
    for r in relation[v]:   # 방문한 정점에 있는 가좍들에 촌수 +1
        if not visit[r]:
            answer[r] = answer[v]+1;
            dfs(r)

dfs(p)
# dfs(q)
if answer[q] > 0: print(answer[q])
else: print(-1)