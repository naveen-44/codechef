def fac(n):
    if n <= 1:
        return 1
    return n*(fac(n-1))
    
t = int(input())
ans = [fac(i) for i in range(101)]

for tt in range(t):
    n = int(input())
    print(ans[n])
