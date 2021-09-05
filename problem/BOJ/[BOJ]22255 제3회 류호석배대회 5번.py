import sys, heapq
input = sys.stdin.readline

N,M = map(int,input().split())
sx,sy,ex,ey = map(int,input().split())
sx-=1; sy-=1; ex-=1; ey-=1
vis , pq = dict(), []
m = [ list(map(int,input().rstrip('\n').split())) for _ in range(N)]
key = (0,1,sx,sy)
vis[(1,sx,sy)] = 0
heapq.heappush(pq, key)
answer = -1
direction1 = 0

def range_check(x,y):
    return 0<=x<N and 0<=y<M

while pq:
    wei, dis, cx, cy = heapq.heappop(pq)
    if cx == ex and cy == ey: 
        answer = wei
        break
    if vis[(dis,cx,cy)] < wei: continue

    if dis%3 == 0: direction = [(-1,0), (0,1), (1,0), (0,-1)]
    elif dis%3 == 1: direction = [(-1,0), (1,0)]
    else: direction = [(0,-1), (0,1)]
    
    for dx, dy in direction:
        nx,ny = cx + dx, cy+ dy
        if not range_check(nx,ny): continue
        if m[nx][ny] == -1: continue
        key = ( (dis+1)%3, nx,ny)
        if key not in vis.keys():
            heapq.heappush(pq, (wei+m[nx][ny], (dis+1)%3, nx,ny))
            vis[key] = wei + m[nx][ny]
        else:
            if vis[key] <= wei+m[nx][ny]: continue
            heapq.heappush(pq,(wei+m[nx][ny] , (dis+1)%3, nx,ny))
            vis[key] = wei + m[nx][ny]

print(answer)