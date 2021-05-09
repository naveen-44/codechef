def fun():
    X,A,B = list(map(int,input().split()))
    ans = A + (100 - X)*B
    print(ans*10)

T = int(input())
for i in range(T):
    fun()
