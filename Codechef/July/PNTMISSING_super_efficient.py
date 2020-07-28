import sys
T=int(input())
for _ in range(T):
    n=int(input())
    x=0
    y=0
    for i in range((4*n)-1):
        a,b=map(int,input().split())
        x=x^a
        y=y^b
    print(x,y)