from collections import deque
N = int(input())
card = deque(range(1, N+1))

if len(card) == 1:
    print(card[0])
else:
    while len(card) > 1:
        card.popleft() # 제일 위 카드 버리고
        if len(card) == 1:
            print(card[0])
            break
        temp = card.popleft()
        card.append(temp)