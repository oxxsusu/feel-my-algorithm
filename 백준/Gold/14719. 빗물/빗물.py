h, w = map(int, input().split())
status = list(map(int, input().split()))

rain = 0
for i in range(1, w-1):
    left, right = max(status[:i]), max(status[i:])
    min_height = min(left, right)
    
    if min_height > status[i]:
        rain += min_height - status[i]
        
print(rain)