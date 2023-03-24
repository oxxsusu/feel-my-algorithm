# 1052

N, K = map(int, input().split())
bottle = N  # 나중에 빼주기 N

if N <= K:
    print(0)
else:
    while bin(N).count('1') > K:
        one_idx = bin(N)[::-1].index('1')
        N += 2**one_idx

    if not bottle:
        print(-1)
    else:
        print(N - bottle)