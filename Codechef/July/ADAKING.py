import sys
T = int(input())
for _ in range(T):
    n=int(input())
    n-=1
    for i in range(8):
        for j in range(8):
            if(i==0 and j==0):
                print('O',end='')
            else:
                if(n>0):
                    n=n-1
                    print('.',end='')
                else:
                    print('X',end='')
        print(' ') 