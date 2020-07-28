import sys
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    total=0
    for i in l:
        if(i>b):
            total+=b-i
    print(abs(total))