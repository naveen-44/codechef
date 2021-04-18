T = int(input())
for t in range(T):
  w1,w2,x1,x2,M = list(map(int,input().split()))
  p1 = w1 + (x1*M)
  p2 = w1 + (x2*M)
  if w2 >= p1 and w2 <= p2:
    print(1)
  else:
    print(0)
