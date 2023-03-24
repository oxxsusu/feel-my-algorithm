# 5545

N = int(input())    # 토핑 종류
A, B = map(int, input().split())    # 도우 가격, 토핑 가격
C = int(input())    # 도우 열량
D = sorted([int(input()) for _ in range(N)], reverse=True)    # 각각 토핑 열량
cal_per_won = []

for i in range(N+1):
    price = A + B*i
    toppings = D[:i]   # i개의 토핑을 뽑은 조합
    calories = sum(toppings) + C
    cal_per_won.append(calories // price)

print(max(cal_per_won))