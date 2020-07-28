import sys
t=int(input())
for _ in range(t):
    n=int(input())
    l=[]
    cur=1
    for i in range(n):
        k=[]
        for j in range(n):
            k.append(cur)
            cur+=1
        if(i%2==1):
            l.append(k[::-1])
        else:
            l.append(k)
    for i in l:
        for j in i:
            print(j,end=" ")
        print(" ")