N = int(input())
balls = list(input())
red, blue = balls.count('R'), balls.count('B')
left, right, lf, rf = 0, 0, balls[0], balls[N-1]
ans = min(red, blue)

# 왼쪽 확인
for ball in balls:
    if ball != lf: break
    left += 1
if lf == 'R':
    ans = min(ans, red - left) #1
else:
    ans = min(ans, blue - left) #2

# 오른쪽 확인
for ball in reversed(balls):
    if ball != rf: break
    right += 1
if rf == 'R':    #3
    ans = min(ans, red - right)
else:    #4
    ans = min(ans, blue - right)

print(ans)