import sys

S = set()
t = int(sys.stdin.readline().strip())

for _ in range(t):
    text = sys.stdin.readline().strip().split()
    if text[0] == "all":
        S = set(range(1, 21))
        continue
    elif text[0] == "empty":
        S = set()
        continue

    command, x = text[0], text[1]
    x = int(x)
    if command == "add":
        S.add(x)
    elif command == "remove":
        S.discard(x)
    elif command == "check":
        if x in S:
            print(1)
        else:
            print(0)
    elif command == "toggle":
        if x in S:
            S.discard(x)
        else:
            S.add(x)