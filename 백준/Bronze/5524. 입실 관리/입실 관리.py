import sys
def input():
    return sys.stdin.readline()

N = int(input())
for _ in range(N):
    print(input().strip().lower())