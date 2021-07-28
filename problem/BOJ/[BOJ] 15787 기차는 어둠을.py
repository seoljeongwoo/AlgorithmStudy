import sys
N = 0
[N,M] = map(int,sys.stdin.readline().split())

v = [0 for _ in range(N + 1)]
j = 0
s = set()
while M > j:
  ca = list(map(int,sys.stdin.readline().split()))
  case = ca[0]
  i = ca[1]
  if case == 1:
    v[i] = v[i] | 1 << (ca[2] - 1)
  
  elif case == 2:
    v[i] = v[i] & ~(1 << (ca[2] - 1))

  elif case == 3:
    v[i] = v[i] << 1
    v[i] = v[i] & ((1<<20)-1)
  elif case == 4:
    v[i] = v[i] >> 1

  j = j + 1

for i in range(1,len(v)):
  s.add(v[i])

print(len(s))

## 너무나 어렵다 비트연산 문제 
## 비트로 풀어야 하겠다는 생각은 했지만 짤 때 너무 어려웠다.
##  N^2 => N 으로 바꿔야 하는 생각으로 시간을 너무 많이 소모