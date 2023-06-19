n = int(input())
t = [0 for _ in range(n+1)]
t[0] = 1

for i in range(1, n+1):
    if i==1:
        t[i] = 1
    else:
        t[i] = t[i-1]+t[i-2]

print(t[n]%10007)