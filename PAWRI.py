def fun(s):
  xx = 'party'
  x = []
  for i in s:
    x.append(i)
    
  for i in range(len(s)-4):
    if(s[i:i+5] == xx):
      x[i+2] = 'w'
      x[i+3] = 'r'
      x[i+4] = 'i'
  g = ''
  for gg in x:
    g+=gg
  return g

n = int(input())
for t in range(n):
  s = input()
  ans = fun(s)
  print(ans)
