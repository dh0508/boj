import sys
def input():
    return sys.stdin.readline()

a,b,c = map(int, input().strip().split())

if a==b and b==c:
    print(10000+a*1000)
elif a==b:
    print(1000+a*100)
elif b==c:
    print(1000+b*100)
elif a==c:
    print(1000+a*100)
else:
    print(max([a,b,c])*100)