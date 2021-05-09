def fun():
    n,x,k = list(map(int,input().split()))
    if x == 0 or x == n+1:
        return True
    
    if x%k == 0:
        return True
    if (n+1 -x) % k == 0:
        return True
    return False

T = int(input())
for i in range(T):
    if fun() == True:
        print("YES")
    else:
        print("NO")
        
