import sys
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l1=[]
    i=0
    while(i<len(l)):
        l1.append(l[i])
        if(i+1 <len(l)):
            if(l[i+1]==l[i]):
                i+=1
        i+=1
            
    mx=0
    res=l1[0]
    for i in l1:
        freq=l1.count(i)
        if(freq>mx or (freq==mx and i<res)):
            res=i
            mx=freq
    print(res)
            
        