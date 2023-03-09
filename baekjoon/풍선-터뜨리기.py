from collections import *

N = int(input())
pop_list = list(map(int, input().split()))

answer = [1]  # 1번 풍선 먼저 pop
pop = pop_list[0]
pop_list[0] = 0
ptr = 0

while pop_list != [0 for i in pop_list]:
    if pop > 0:  # 이동수가 양수이면
        while pop != 0:
            ptr += 1
            if pop_list[ptr % N] != 0:
                pop -= 1

        pop = pop_list[ptr % N]
        answer.append(ptr % N + 1)
        pop_list[ptr % N] = 0

    else:
        while pop != 0:
            ptr -= 1
            if pop_list[ptr % N] != 0:
                pop += 1

        pop = pop_list[ptr % N]
        answer.append(ptr % N + 1)
        pop_list[ptr % N] = 0

print(*answer)
