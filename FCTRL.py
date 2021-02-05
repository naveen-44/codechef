t = int(input())
while(t):
    x = int(input())
    n = 5
    ans = 0
    while(x/n>=1):
        ans += int(x/n)
        n *= 5
    print(ans)
    t-=1
