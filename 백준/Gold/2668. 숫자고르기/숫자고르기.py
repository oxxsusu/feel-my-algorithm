n = int(input())
a = [i for i in range(n)]
b, ans = [], []
for i in range(n):
    b.append(int(input())-1)

def dfs(start, route):
    if len(route) > n:
        return

    end = route[len(route)-1]
    if start == b[end]:
        route.append(b[end])
        for r in route:
            if r not in ans:
                ans.append(r)
                
    else:
        route.append(b[end])
        dfs(start, route)

for i in range(n):
    dfs(i, [i])

ans.sort()
print(len(ans))
for i in range(len(ans)):
    ans[i] += 1
    print(ans[i])