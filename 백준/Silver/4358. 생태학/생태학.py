import sys
d = dict()

while True:
    tree = sys.stdin.readline().rstrip()
    if not tree:
        break
    if tree not in d.keys():
        d[tree] = 1
    else:
        d[tree] += 1

total = sum(d.values())
tree_list = list(d.keys())
tree_list.sort()
for t in tree_list:
    print("%s %.4f"%(t, d[t]/total*100))