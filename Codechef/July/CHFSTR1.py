import sys
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    s=0
    for i in range(len(l)-1):
        s+=abs(l[i+1]-l[i])
    print(s-n+1)