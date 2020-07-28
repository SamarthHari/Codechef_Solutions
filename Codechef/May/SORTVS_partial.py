import sys
def minSwaps(arr):  #idea from https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/
    n = len(arr) 
    arrpos = [*enumerate(arr)] 

    arrpos.sort(key = lambda it:it[1]) 

    vis = {k:False for k in range(n)} 

    ans = 0
    for i in range(n): 
        if vis[i] or arrpos[i][0] == i: 
            continue
        cycle_size = 0
        j = i 
        while not vis[j]: 
            vis[j] = True
            j = arrpos[j][0] 
            cycle_size += 1
        if cycle_size > 0: 
            ans += (cycle_size - 1) 
    return ans 
T=int(input())
for _ in range(T):
    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    l1=[]
    for i in range(m):
        a,b=map(int,input().split())
        l1.append(tuple((a-1,b-1)))
    t=0
    count=0
    while(t<n and count<n**3):
        t=0
        for i in range(n-1):
            if(l[i]>l[i+1]):
                if((i,i+1) in l1):
                    l[i],l[i+1]=l[i+1],l[i]
            else:
                t+=1
        count+=1
    minutes=minSwaps(l)
    print(minutes)
            
        