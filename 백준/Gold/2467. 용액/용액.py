n = int(input())
s = list(map(int, input().split()))

s1, s2 = 0, 0
ans = float('inf')      # 두 용액을 섞은 결과 -> 비교용 무한

for i in range(n-1):
    start = i+1
    end = n-1
    cur = s[i]  # 지금 쥐고 있는 용액

    # bs
    while start <= end:
        mid = (start+end)//2
        temp = cur + s[mid] # 지금 쥐고 있는 용액과 중간값을 섞음

        if abs(temp) < ans:
            ans = abs(temp)
            s1, s2 = cur, s[mid]
            if temp == 0:
                break

        # 합친 게 음수였으면 더 큰 값 (오른쪽으로)
        if temp < 0:
            start = mid + 1

        else:
            end = mid - 1

print(min(s1, s2), max(s1, s2))