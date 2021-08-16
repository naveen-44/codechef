## In Olympics, the countries are ranked by the total number of medals won.
## You are given six integers G1, S1, B1, and G2, S2, B2, the number of gold, silver and bronze medals won by two different countries respectively.
## Determine which country is ranked better on the leaderboard. 
## It is guaranteed that there will not be a tie between the two countries.

n = int(input())
for i in range(n):
    l = list(map(int, input().split()))
    s1 = sum(l[:3])
    s2 = sum(l[3:])
    if s1>s2:
        print(1)
    else:
        print(2)
