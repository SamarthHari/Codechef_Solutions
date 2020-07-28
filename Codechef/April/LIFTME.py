T=int(input())
for _ in range(T):
    n,q=map(int,input().split())
    sum=0
    cur=0
    for i in range(q):
        a,b=map(int,input().split())
        sum+=abs(cur-a)+abs(a-b)
        cur=b
    print(sum)