import sys
T=int(input())
for _ in range(T):
    n=int(input())
    l=list(map(int,input().split()))
    places=[]
    while(1 in l):
        ind=l.index(1)
        places.append(ind)
        l[ind]=0
    k=0
    for i in range(1,len(places)):
        if(k>0):
            break
        else:
            if(places[i]-places[i-1]<6):
                k+=1
                print("NO")
    if(k==0):
        print("YES")