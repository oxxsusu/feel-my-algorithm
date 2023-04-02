import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    trees = sorted(list(map(int, input().split())), reverse=True)

    front, back = [trees.pop()], [trees.pop()]
    while len(trees) > 1: 
        front.append(trees.pop())
        back.append(trees.pop())
    if trees:
        front.append(trees.pop())
    back.reverse()
    new_trees = front + back

    df = [abs(new_trees[n-1]-new_trees[0])]
    for i in range(1, n):
        df.append(abs(new_trees[i]-new_trees[i-1]))
    print(max(df))