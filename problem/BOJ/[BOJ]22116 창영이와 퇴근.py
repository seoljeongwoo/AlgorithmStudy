import sys, heapq
input = sys.stdin.readline

N = int(input())
A = [list(map(int,input().rstrip('\n').split())) for _ in range(N)]
DP = dict()

pq = []
heapq.heappush(pq , (0,0,0))
DP[(0,0)] = 0
while pq:
    w,x,y = heapq.heappop(pq)
    if x == N-1 and y == N-1: break
    if DP[(x,y)] < w : continue
    for dx,dy in [(-1,0), (1,0), (0,1) ,(0,-1)]:
        nx,ny = x+dx, y+dy
        if 0<=nx<N and 0<=ny<N:
            gap = max(w,abs(A[nx][ny] - A[x][y]))
            if (nx,ny) not in DP.keys() or DP[(nx,ny)] > gap:
                DP[(nx,ny)] = gap
                heapq.heappush(pq, (gap, nx,ny))
print(DP[(N-1,N-1)])

