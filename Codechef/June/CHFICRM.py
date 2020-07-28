import sys
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    count=[0,0,0]
    yorno=True
    for i in l:
        if(yorno==False):
            break
        if (i==5):
            count[0]+=1
            continue
        elif(i==10):
            if(count[0]==0):
                yorno=False
                break
            else:
                count[0]-=1
                count[1]+=1
                continue
        elif(i==15):
            if(count[1]==0 and count[0]<2):
                yorno=False
                break
            else:
                count[2]+=1
                if(count[1]>0):
                    count[1]-=1
                else:
                    count[0]-=2
    if(yorno==True):
        print("YES")
    else:
        print("NO")