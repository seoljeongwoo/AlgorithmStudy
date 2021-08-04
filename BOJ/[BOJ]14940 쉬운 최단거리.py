import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
lst = []
result = [[-1]*m for _ in range(n)]
for _ in range(n):
    lst.append(list(map(int,input().rstrip('\n').split())))
def search():
    for row in range(n):
        for col in range(m):
            if lst[row][col] == 2: 
                return row,col
tx,ty = search()
que =deque()
que.append((tx,ty))
result[tx][ty] = 0
def range_check(x,y):
    return 0<=x<n and 0<=y<m
while que:
    cx,cy = que.popleft()
    for dx,dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx,ny = cx+dx , cy+dy
        if not range_check(nx,ny) : continue
        if result[nx][ny] != -1 or lst[nx][ny] == 0: continue
        result[nx][ny] = result[cx][cy] + 1
        que.append((nx,ny))

for row in range(n):
    for col in range(m):
        if result[row][col] != -1:
            print(result[row][col], end = ' ')
        else:
            print(0 if lst[row][col] == 0 else -1, end = ' ')
    print()