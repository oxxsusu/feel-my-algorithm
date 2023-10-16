from collections import deque

N, K = map(int, input().split())
MAX = 10**6
visit = [False] * (MAX*2 + 1)

q = deque()
visit[N] = True
q.append((0, N))

while q:
    time, idx = q.popleft()
    if idx == K: print(time); break

    if idx > MAX or idx < 0: continue

    # [순간이동] 시간이 적게 들어서 최소시간이 되므로 appendleft 처리
    if not visit[idx*2]:
        visit[idx*2] = True
        q.appendleft((time, idx*2))

    if not visit[idx-1]:
        visit[idx-1] = True
        q.append((time+1, idx-1))

    if not visit[idx+1]:
        visit[idx+1] = True
        q.append((time+1, idx+1))


