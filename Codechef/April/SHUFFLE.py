import sys
T=int(input())
for _ in range(T):
    n,k= map(int,input().split())
    l= list(map(int,input().split()))
    for i in range(int(n**0.5)*2):
        for j in range(n-k):
            if(l[j]>l[j+k]):
                l[j],l[j+k]=l[j+k],l[j]
    if(k==1):
        print("yes")

    elif(l==sorted(l)):
        print("yes")
    else:
        print("no")