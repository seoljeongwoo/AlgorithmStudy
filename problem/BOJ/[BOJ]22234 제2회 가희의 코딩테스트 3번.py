import sys, heapq
from collections import deque
input = sys.stdin.readline

N,T,W = map(int,input().rstrip('\n').split())
que = deque()
for _ in range(N):
    px,tx = map(int,input().rstrip('\n').split())
    que.append((px,tx))
M = int(input())
pq = []
for _ in range(M):
    px, tx, cx = map(int,input().rstrip('\n').split())
    heapq.heappush(pq, (cx,px,tx))
curr_time = 0
while curr_time < W:
    p,t = que.popleft()
    if t > T:
        for i in range(T):
            print(p)
            curr_time += 1
            if curr_time >= W: break
    else:
        for i in range(t):
            print(p)
            curr_time += 1
            if curr_time >= W: break

    while pq and pq[0][0] <= curr_time:
        cx,px,tx = heapq.heappop(pq)
        que.append((px,tx))

    if t > T:
        que.append((p, t-T))
