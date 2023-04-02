import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())
ans, start, end = 0, 0, n-1

while start < end:
    temp = arr[start] + arr[end]
    if temp == x:
        ans += 1
        start += 1
    elif temp < x:
        start += 1
    elif temp > x:
        end -= 1

print(ans)