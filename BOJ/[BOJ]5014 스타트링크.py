import sys
from collections import deque
input = sys.stdin.readline

F,S,G,U,D = map(int,input().rstrip('\n').split())
vis = [-1]*(F+1)
que = deque()
que.append(S)
vis[S] = 0
def range_check(floor):
    return 0 < floor <= F
while que:
    curr = que.popleft()
    next_upstair = curr + U
    next_downstair = curr - D
    if range_check(next_upstair):
        if vis[next_upstair] == -1:
            vis[next_upstair] = vis[curr] + 1
            que.append(next_upstair)
    if range_check(next_downstair):
        if vis[next_downstair] == -1:
            vis[next_downstair] = vis[curr] + 1
            que.append(next_downstair)
print(vis[G] if vis[G] != -1 else 'use the stairs')



