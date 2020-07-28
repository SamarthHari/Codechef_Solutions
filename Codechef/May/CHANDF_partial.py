import sys
import math
T=int(input())
for _ in range(T):
    a,b,left,right=map(int,input().split())
    if(a==0 or b==0):
        print(0)
    else:
        if(a|b>=left and a|b<=right):
            print(a|b)
        else:
            k=a|b
            while(True):
                if(k<left):
                    k=k|left
                else:
                    p=k&(~right)
                    if(p<=right):
                        k=p
                        if(p>=left):
                            break
                    else:
                        p=int(math.log(k-right,2))+1
                        t=(2**int(math.log(((k//(2**p))&(-(k//(2**p)))),2)+p))
                        k=k&(~t)
            print(k)
                        
                    
                            
            