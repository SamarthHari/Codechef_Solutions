import sys
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    count=0
    p1=0
    p2=0
    start=0
    while (start+1<a and l[start]<b):
        start += 1
    if(start > 0):
        p2 = 1
        temp = b
        while(temp<l[start]):
            temp*=2
            p1+=1
        temp=l[start-1]
        temp*=2
        while(temp<l[start]):
            temp*=2
            p2+=1
        if(p2<=p1):
            start-=1
    s=start-1
    while(start<a):
        count += 1
        if(b >= l[start]):
            b=l[start]
            l[start]=0
            start+=1
        b*=2
    while(s>=0):
        count+= 1
        if(b>=l[s]):
            b=l[s]
            l[s]=0
            s-=1
        b*=2
    print(count)  