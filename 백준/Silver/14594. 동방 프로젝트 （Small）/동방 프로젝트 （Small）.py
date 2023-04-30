N = int(input())
M = int(input())
action = [map(int, input().split()) for _ in range(M)]
room = [1 for i in range(N+1)]

for x, y in action:
    for i in range(x+1, y+1):
        room[i] = 0

room.pop(0)
print(room.count(1))