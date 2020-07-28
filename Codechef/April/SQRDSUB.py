import sys
T=int(input())
for _ in range(T):
    n=int(input())
    l=[]
    lb=0
    ub=0
    lbub=0
    curr=0
    total=int((n*(n+1))/2)
    l1=list(map(int,input().split()))
    for a in l1:
        if(a%2==0 and a%4!=0):
            l.append(1)
        elif(a%4==0):
            l.append(2)
        else:
            l.append(0)
    lb=1
    for i in range(n):
        curr+=l[i]
        if(curr==1):
            ub+=1
        elif(curr==0):
            lb+=1
        elif(curr==2):
            if(l[i]==1):
                lbub+=(lb*ub)
                lb=ub
                curr=1
                ub=1
            elif(l[i]==2):
                ub=0
                curr=0
                lb=1
        else:
            lbub+=(lb*ub)
            lb=1
            ub=0
            curr=0
        
    if(curr!=1):
        print(total-lbub)
    else:
        print(total-lbub-(lb*ub))
        
        
            
                
                
    
