import sys
import heapq
input = sys.stdin.readline


N,L = map(int,input().split())
lst = list(map(int,input().rstrip('\n').split()))
pq = []
for data in lst:
    heapq.heappush(pq, data*10)
    
pos = 0
ret = 0
while pq:
    top = heapq.heappop(pq)
    if pos >= top + 5: continue
    else:
        ret += 1
        pos = top - 5 + 10*L
print(ret)