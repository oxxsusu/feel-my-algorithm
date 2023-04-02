import sys
input = sys.stdin.readline

N, K = map(int, input().split())
kids = list(map(int, input().split()))

costs = []
for i in range(N-1):
    costs.append(kids[i+1] - kids[i])
costs.sort()

print(sum(costs[:N-K]))