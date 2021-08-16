## Chef is trying to invent the light bulb that can run at room temperature without electricity. 
## So he has N gases numbered from 0 to N−1 that he can use and he doesn't know which one of the N gases will work but we do know it.
## Now Chef has worked on multiple search algorithms to optimize search. For this project, he uses a modulo-based search algorithm that he invented himself. 
## So first he chooses an integer K and selects all indices i in increasing order such that imodK=0 and test the gases on such indices, then all indices i in increasing order such that imodK=1, and test the gases on such indices, and so on.
## Given N, the index of the gas p that will work, and K, find after how much time will he be able to give Chefland a new invention assuming that testing 1 gas takes 1 day.

def newSolveBulb(n,p,k):
    ans = 0
    mval = p%k - 1
    mul = (n-1)//k + 1
    q = (mul - 1)*k
    midk = n - q - 1
    if mval <= midk:
        ans = (mval+1)*mul
        ans+= p//k
        ans += 1
        return ans
    ans = (midk+1)*mul
    ans += (mval - midk)*(mul - 1)
    ans += p//k
    ans += 1
    return ans

t = int(input())
for tt in range(t):
    n,p,k = list(map(int,input().split()))
    result = newSolveBulb(n,p,k)
    print(result)
