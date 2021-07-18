import sys

size = int(sys.stdin.readline())
step = list(map(int,sys.stdin.readline().split()))
jump = [-1] * size

jump[size - 1] = 0
for i in range(size-2,-1,-1):
  cache = 987654321
  for j in range(1,step[i] + 1):
    if i + j > size - 1 :
      break
    else:
      cache = min(cache,jump[i + j])
  if cache == 987654321:
    jump[i] = 987654321
  else:
    jump[i] = 1 + cache

if jump[0] == 987654321:
  print(-1)
else:
  print(jump[0])
  

