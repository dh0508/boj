import sys
def input():
    return sys.stdin.readline()

n = int(input())
l = []
pl = [0 for _ in range(n)]
for _ in range(n):
    x, y = map(int,input().strip().split())
    l.append([x,y])
for i in l:
    rank = 1
    for j in l:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = ' ')