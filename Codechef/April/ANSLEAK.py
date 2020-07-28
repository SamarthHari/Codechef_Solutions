
import sys
import math as mt 
def mostFrequent(arr, n): 
    Hash = dict() 
    for i in range(n): 
        if arr[i] in Hash.keys(): 
            Hash[arr[i]] += 1
        else: 
            Hash[arr[i]] = 1
    max_count = 0
    res = -1
    for i in Hash:  
        if (max_count < Hash[i] or (max_count== Hash[i] and i>res)):  
            res = i 
            max_count = Hash[i] 
    return res  
T=int(input())
l=[]
for _ in range(T):
    N,M,K=map(int,input().split())
    for i in range(N):
        p=list(map(int,input().split()))
        l.append(mostFrequent(p,len(p)))
for i in l:
    print(i,end=" ")
    