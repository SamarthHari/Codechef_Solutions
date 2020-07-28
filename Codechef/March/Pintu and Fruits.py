t=int(input())
while(t!=0):
    n,m=map(int,input().split())
    fruits=list(map(int,input().split()))
    prices=list(map(int,input().split()))
    seen=[]
    sums=[]
    for i in fruits:
        if i in seen:
            continue
        else:
            total=0
            seen.append(i)
            for j in range(len(fruits)):
                if(fruits[j]==i):
                    total=total+prices[j]
            sums.append(total)
    print(min(sums))
    t=t-1
            
        