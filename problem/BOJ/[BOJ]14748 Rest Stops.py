import sys, heapq
input = sys.stdin.readline

L,N,f,b = map(int,input().rstrip('\n').split())
pq = []
for _ in range(N):
    x,c =map(int,input().split())
    heapq.heappush(pq, (-1*c, x))

pos , ret = 0, 0
while pq:
    c,x = heapq.heappop(pq)
    if pos >= x: continue
    dis = (pos-x)*(f-b)
    ret += c*dis
    pos = x
print(ret) 