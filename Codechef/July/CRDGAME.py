import sys
t=int(input())
def calc(n):
    s=0
    while(n>0):
        s+=n%10
        n=n//10
    return s
for _ in range(t):
    n=int(input())
    l=[0,0]
    for i in range(n):
        a,b=map(int,input().split())
        a=calc(a)
        b=calc(b)
        if(a>b):
            l[0]+=1
        elif(a<b):
            l[1]+=1
        else:
            l[0]+=1
            l[1]+=1
    if(l[0]>l[1]):
        print(0,l[0])
    elif(l[1]>l[0]):
        print(1,l[1])
    else:
        print(2,l[0])