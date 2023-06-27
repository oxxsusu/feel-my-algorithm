t = int(input())

for _ in range(t):
    n = int(input())
    stock = list(map(int, input().split()))
    max_stock = stock[-1]   # 뒤에서부터 조회한 최대값
    result = 0

    for i in range(n-2, -1, -1):
        if stock[i] > max_stock:    # 앞 날짜로 갈수록 최대값이 올라가면 갱신
            max_stock = stock[i]
        p = max_stock - stock[i]
        if p > 0:
            result += p

    print(result)