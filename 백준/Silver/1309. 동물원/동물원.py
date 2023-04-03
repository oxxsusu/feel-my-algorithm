import sys
input = sys.stdin.readline

N = int(input())
ans = [3, 7] # N=1일때

for i in range(3, N+1):     # 3부터 N까지
    a, b = ans.pop(), ans.pop()
    ans.append(a)
    ans.append(b+2*a)

if N==1:
    print(3)
else:
    print(ans[1]%9901)