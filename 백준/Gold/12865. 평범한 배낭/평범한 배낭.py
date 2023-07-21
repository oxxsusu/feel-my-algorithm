N, K = map(int, input().split())
wv = [tuple(map(int,input().split())) for _ in range(N)]
wv.append((0, 0))
wv.sort(key=lambda x:x[0])
case = [[0 for _ in range(K+1)] for _ in range(N+1)]

for n in range(1,N+1):  # (무게, 가치) 쌍
    for k in range(1,K+1):  # 최대 가방 무게, k는 현재 가방의 무게
        w, v = wv[n][0], wv[n][1]

        if w <= k:
            case[n][k] = max(case[n-1][k], v+case[n-1][k-w])
        else:
            case[n][k] = case[n-1][k]

print(case[N][K])