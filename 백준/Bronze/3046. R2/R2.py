import sys
def input():
    return sys.stdin.readline()

R1, S = map(int, input().strip().split())
print(2*S - R1)