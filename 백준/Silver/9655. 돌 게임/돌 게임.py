import sys
input = sys.stdin.readline

rock = int(input())
s, c = "SK", "CY"

turn = s
race = rock//3 + rock%3

while race:
    if turn == s:
        turn = c
    elif turn == c:
        turn = s
    race -= 1

if turn == s:
    print(c)
else:
    print(s)