import sys
t=int(input())
for _ in range(t):
    n=int(input())
    if(n%2==1):
        print((n-1)//2)
    else:
        count=0
        l=[n,n]
        while(l[0]%2==0):
            l[0]=l[0]//2
            count+=1
        print((l[1]//2**count)//2)