# 12865

N, K = map(int, input().split())
wv = [tuple(map(int,input().split())) for _ in range(N)]
wv.append((0, 0))
wv.sort(key=lambda x:x[0]) # 무게가 높은 순으로 정렬
case = [[0 for _ in range(K+1)] for _ in range(N+1)]

# DP + 배낭 풀이
for n in range(1,N+1):  # (무게, 가치) 쌍
    for k in range(1,K+1):  # 최대 가방 무게, k는 현재 가방의 무게
        w, v = wv[n][0], wv[n][1]   # 물건을 하나씩 들고 오면서 무게가 0일 때부터 K일 때까지 경우를 파악

        if w <= k:  # 지금 들고 있는 물건이 가방보다 작으면, 넣을 수 있겠지요
            case[n][k] = max(case[n-1][k], v+case[n-1][k-w])
        else:
            case[n][k] = case[n-1][k]

print(case[N][K])



# 첫 풀이 -> 그리디로 풀면 최적해를 보장하지 못한다고 한다. DP로 풀어야 함
