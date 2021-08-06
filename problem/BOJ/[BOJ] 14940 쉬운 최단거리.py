import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())

land = [[ -1 for _ in range(M)] for _ in range(N)]
v = [[False for _ in range(M)] for _ in range(N)]
queue = deque()

dx = [-1,0,1,0]
dy = [0,1,0,-1]

x,y = 0,0

def bfs(i,j):
  v[i][j] = True
  land[i][j] = 0
  queue.append((i,j,0))
  while queue:
    (ix,iy,val) = queue.popleft()
    land[ix][iy] = val
    for a in range(4):
      x = ix + dx[a]
      y = iy + dy[a]
      if 0 <= x < N and 0<= y < M and v[x][y] == False and land[x][y] != 0:
        queue.append((x,y,val + 1))
        v[x][y] = True
    

for i in range(N):
  item = list(map(int,sys.stdin.readline().split()))
  for j in range(M):
    if item[j] == 0:
      land[i][j] = 0
    if item[j] == 2:
      x = i
      y = j

bfs(x,y)

for i in range(N):
  for j in range(M):
    print(land[i][j],end=' ')
  print(end='\n')


  ## N,M 을 반대로 적어서 조금 해맸다.
  ## O(N + M) ?