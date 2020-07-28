t=int(input())
while(t>0):
    n=int(input())
    s=input()
    l=[]
    l.append(s[0])
    for i in s:
        if(l[len(l)-1]=='L' or l[len(l)-1]=='R'):
            if(i=='U' or i=='D'):
                l.append(i)
            else:
                continue
        elif(l[len(l)-1]=='U' or l[len(l)-1]=='D'):
            if(i=='L' or i=='R'):
                l.append(i)
            else:
                continue
    lr=0
    ud=0
    for i in l:
        if(i=='L'):
            lr=lr-1
        elif(i=='R'):
            lr=lr+1
        elif(i=='U'):
            ud=ud+1
        elif(i=='D'):
            ud=ud-1
    print(lr,ud)
        
    t=t-1