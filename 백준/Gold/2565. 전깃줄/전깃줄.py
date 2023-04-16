n = int(input())
cross = [tuple(map(int, input().split())) for _ in range(n)]

cross.sort(key=lambda x:x[0])
dp = [1 for _ in range(n)]  # 자신을 포함해 만들 수 있는 가장 큰 부분수열 크기를 담을 dp 배열
for i in range(n):
    for j in range(i):
        if cross[i][1] > cross[j][1]:   # 뒤에가 나보다 크다면
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))