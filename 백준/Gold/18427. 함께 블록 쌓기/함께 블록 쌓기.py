n, m, h = map(int, input().split())
dp = [[1]+[0]*h for _ in range(n+1)]    # 가로축 블럭번호, 세로축 학생번호

for i in range(1, n+1):
    for j in range(1, h+1): # 이전 번호 학생의 경우의 수 그대로 복사
        dp[i][j] = dp[i-1][j]
    blocks = list(map(int, input().split()))
    for block in blocks:    # 블럭 번호와
        for k in range(block, h+1): # 해당 블럭을 들고 있다고 생각하고, h까지 경우의 수 계산
            dp[i][k] += dp[i-1][k-block]

print(dp[-1][-1] % 10007)