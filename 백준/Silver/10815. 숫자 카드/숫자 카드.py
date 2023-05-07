N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
numbers = list(map(int, input().split()))

def bs(target):
    start = 0
    end = N-1

    if target < cards[start] or target > cards[end]:
        return False

    while start <= end:
        mid = (start+end) // 2
        if cards[mid] == target:
            return True
        elif cards[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return False

answer = []
for number in numbers:
    if bs(number):
        answer.append(1)
    else:
        answer.append(0)

print(*answer)