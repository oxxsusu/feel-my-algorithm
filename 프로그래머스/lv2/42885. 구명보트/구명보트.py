from collections import deque

def solution(people, limit):
    answer = 1
    boat = []
    people.sort()
    people = deque(people)

    while people:
        first = people.pop()
        boat.append(first)
        while people:    # 다음 탈 사람이 존재하는 경우
            next = people[0]
            if len(boat)<2 and boat[0] + next <= limit:
                boat.append(people.popleft())
            else:
                answer += 1
                boat.clear()
                break
    
    return answer