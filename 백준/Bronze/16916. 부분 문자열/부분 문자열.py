import sys
def input():
    return sys.stdin.readline()

S = input().strip()
P = input().strip()

if P in S:
    print(1)
else:
    print(0)