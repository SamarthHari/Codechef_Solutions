import sys
t=int(input())
for _ in range(t):
    s=input()
    s1=s[1:]+s[0]
    s2=s[-1]+s[:len(s)-1]
    if(s1==s2):
        print("YES")
    else:
        print("NO")