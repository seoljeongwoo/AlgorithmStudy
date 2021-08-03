import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().rstrip('\n').split())
edge = [ [] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,input().rstrip('\n').split())
    edge[u].append(v)
    edge[v].append(u)

def dist(a,b):
    que = deque()
    vis = [-1]*(N+1)
    vis[a] , vis[b] = 0, 0
    que.append(a)
    que.append(b)
    while que:
        curr= que.popleft()
        for nx in edge[curr]:
            if vis[nx] != -1:
                continue
            vis[nx] = vis[curr] + 1
            que.append(nx)
    dis = sum(vis[1:])
    return (dis, a, b)

ret = (int(1e9), N+1, N+1)
for first in range(1,N+1):
    for second in range(first+1, N+1):
        subRet = dist(first, second)
        if ret > subRet:
            ret = subRet
print(ret[1], ret[2], ret[0]*2)