import sys
T=int(input())
for _ in range(T):
    n=int(input())
    cars=list(map(int,input().split()))
    profit=0
    cars.sort(reverse=True)
    for i,car in enumerate(cars):
        if(car-i>0):
            profit+=car-i
    print(profit%1000000007)
        