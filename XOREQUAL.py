MOD = 10**9 + 7
def fastpow(a,n):
    if n==1:
        return a
    if n==0:
        return 1
    t = fastpow(a,n//2)
    p = (t*t)%MOD
    if n%2==1:
        p= (p*a)%MOD
    return p%MOD
def fun(N):
    count = 0
    for x in range(2**(N)):
        x1 = x^(x+1)
        x2 = (x+2)^(x+3)
        if x1==x2:
            count+=1
    return count
        
T = int(input())
for i in range(T):
    N = int(input())
    print(fastpow(2,N-1))
        
