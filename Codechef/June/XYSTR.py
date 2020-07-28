import sys
t=int(input())
for _ in range(t):
    s=input()
    i=0
    count=0
    while(i<len(s)-1):
        if(s[i]=='x'):
            i+=1
            if(s[i]=='y'):
                count+=1
                i+=1
        elif(s[i]=='y'):
            i+=1
            if(s[i]=='x'):
                count+=1
                i+=1
    print(count)