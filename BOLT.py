T = int(input())
for t in range(1,T+1):
    a,b,c,v = list(map(float,input().split()))
    x = a*b*c*v
    tt = 100/x
    tt = round(tt,2)
    if(tt<9.58):
        print("YES")
    else:
        print("NO")
      
