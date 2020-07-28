import sys
T=int(input())
for _ in range(T):
    n,q=map(int,input().split())
    s=input()
    l=[0]*26
    for i in s:
        l[int(ord(i)-ord('a'))]+=1
    for i in range(q):
        c=int(input())
        k=0
        for j in l:
            if(j>c):
                k+=abs(j-c)
        print(k)