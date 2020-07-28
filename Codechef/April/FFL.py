T = int(input())
for _ in range(T):  
    n,s = map(int,input().split())
    l1= list(map(int,input().split()))
    l2= list(map(int,input().split()))
    a=1000000
    b=1000000
    for i in range(n):
        if l2[i] == 0:
            a = min(l1[i],a)
        else:
            b= min(l1[i],b)
    if  (s+a+b<=100):
        print('yes')
    else:
        print('no')