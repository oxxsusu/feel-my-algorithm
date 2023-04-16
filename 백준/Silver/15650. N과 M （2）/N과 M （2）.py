N, M = map(int, input().split())

l = []
visit = [False] * (N+1)     # 수 범위 N, 수열 길이 M

# N까지 돌면서 그 수를 방문하지 않았다면 추가하고, 방문 처리
def dfs(_l, idx):
    if len(l) == M:
        print(' '.join(map(str, l)))
        return  # 꼬오옥!!! 종료 좀 시켜줘...

    for i in range(idx, N+1):
        if visit[i]:
            continue

        visit[i] = True     # 일단 i번째 루프 안으로 고
        l.append(i)
        dfs(_l, i+1)  # 끝자리 (i) 파라미터로 넣어주고 그 이후로 탐색하게
        l.pop()
        visit[i] = False

dfs(l, 1)