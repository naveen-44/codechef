x=0
while(x!=""):
    x = input()
    n = int(x)
    g = max(n, int(n/2) + int(n/3) + int(n/4))
    print(g)
