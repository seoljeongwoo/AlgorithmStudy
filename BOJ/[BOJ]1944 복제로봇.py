import sys
import heapq
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().rstrip('\n').split())
lst = [ list(input().rstrip('\n')) for _ in range(N)]
vertexNumber = 0
posKey = dict()
pq = []

def calc(x,y):
    global vertexNumber, posKey, pq

    if (x,y) not in posKey.keys():
        posKey[(x,y)] = vertexNumber
        vertexNumber += 1

    vis = [ [-1] * N for _ in range(N)]
    vis[x][y] = 0
    que = deque()
    que.append((x,y))
    while que:
        cx,cy = que.popleft()
        for dx,dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx,ny = cx+dx, cy+dy
            if nx <0 or nx >=N or ny <0 or ny >=N :
                continue
            if lst[nx][ny] == '1' or vis[nx][ny] != -1:
                continue
            if lst[nx][ny] == '0':
                vis[nx][ny] = vis[cx][cy] + 1
                que.append((nx,ny))
                continue
            if lst[nx][ny] == 'S' or lst[nx][ny] == 'K':
                vis[nx][ny] = vis[cx][cy] + 1
                que.append((nx,ny))
                if (x,y) not in posKey.keys():
                    posKey[(x,y)] = vertexNumber
                    vertexNumber += 1
                curr_key = posKey[(x,y)]
                if (nx,ny) not in posKey.keys():
                    posKey[(nx,ny)] = vertexNumber
                    vertexNumber += 1
                next_key = posKey[(nx,ny)]
                heapq.heappush(pq, (vis[nx][ny], curr_key, next_key))
    return




for rowIndex,rowData in enumerate(lst):
    for colIndex,colData in enumerate(rowData):
        if colData =='S' or colData =='K':
            calc(rowIndex, colIndex)

cnt ,result =0, 0
parent = [i for i in range(vertexNumber)]
def pa(v):
    global parent
    if parent[v] != v:
        parent[v] = pa(parent[v])
    return parent[v]

def uf(v,w):
    global parent
    v = pa(v)
    w = pa(w)
    parent[v] = w
    return

while pq:
    wei , v1, v2 = heapq.heappop(pq)
    if pa(v1) == pa(v2):
        continue
    cnt +=1
    result += wei
    uf(v1,v2)
print(result if cnt == M else -1)
