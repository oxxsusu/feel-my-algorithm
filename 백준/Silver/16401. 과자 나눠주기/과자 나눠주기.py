M, N = map(int, input().split())
snacks = list(map(int, input().split()))

start, end = 1, max(snacks)
answer = 0

while start <= end:
    mid = (start+end)//2

    total = sum([s//mid for s in snacks])
    if total >= M:
        answer = mid
        start = mid+1
    else:
        end = mid-1

print(answer)