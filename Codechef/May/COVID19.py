import sys
T=int(input())
for _ in range(T):
    mn=10000000000
    mx=1
    cur=1
    n=int(input())
    l=list(map(int,input().split()))
    for i in range(n-1):
        if(l[i+1]-l[i]<=2):
            cur+=1
            continue    
        if(cur>mx):
            mx=cur
        if(cur<mn):
            mn=cur
        if(l[i+1]-l[i]>2):
            cur=1
    print(min(cur,mn),max(cur,mx))
    