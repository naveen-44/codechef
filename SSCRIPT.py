T = int(input())
for t in range(1,T+1):
    l,n = list(map(int,input().split()))
    s = input()
    maxn1 = 0
    n1=0
    p = ''
    for i in s:
        if(p=="*" and i=="*"):
            n1+=1
        elif(i=="*"):
            n1=1
            p=i
        else:
            maxn1=max(n1,maxn1)
            p = i
            n1=0

    maxn1 = max(n1,maxn1)
    if(maxn1>=n):
        print("YES")
    else:
        print("NO")
            
