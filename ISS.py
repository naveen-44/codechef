import math
def facs(n):
    fl = []
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            fl.append(i)
            if i*i != n:
                fl.append(n//i)
    fl = sorted(fl)
    return fl

def ffl_do(e,n):
    ffl = []
    fl = facs(e)
    for f in fl:
        ffl.append(n//f)
    for ff1 in range(len(fl)-1,-1,-1):
        f1 = fl[ff1]
        for ff2 in range(ff1-1,-1,-1):
            f2 = fl[ff2]
            if f1%f2==0:
                ffl[ff2]-=ffl[ff1]
    x = sum(ffl)
    ans = e + (n-x) - 1
    for f1 in range(len(fl)):
        ans+= fl[f1]*ffl[f1]
    return ans

def solve(k):
    e = 4*k + 1
    n = 2*k
    ans = ffl_do(e,n)
    return ans
    
t = int(input())
tl = []
kl = []
a = {}
for i in range(t):
    k = int(input())
    tl.append(k)
    if k not in kl:
        kl.append(k)
for k in kl:
    a[k] = [solve(k)]
for k in tl:
    print(a[k][0])
    
