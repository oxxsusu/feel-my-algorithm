N = int(input())
s = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N+1)

for i in range(N):
    for j in range(i+s[i][0], N+1):
        # print(f"i:{i} j:{j}")
        if dp[j] < dp[i] + s[i][1]:
            dp[j] = dp[i] + s[i][1]
            # print(dp)

print(dp[N])
