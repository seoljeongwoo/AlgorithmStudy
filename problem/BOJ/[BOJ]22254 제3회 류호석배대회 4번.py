import sys, heapq

N,X = map(int,input().split())
lst = list(map(int,input().rstrip('\n').split()))

lo ,hi = 0, 100001
answer = 0
def solve(v):
    if v == 0: return False
    pq = []
    for i in range(v):
        heapq.heappush(pq, 0)
    for data in lst:
        a = heapq.heappop(pq)
        a += data
        heapq.heappush(pq, a)
    return True if max(pq) <= X else False
    
while lo <= hi:
    mid = (lo+hi)//2
    if solve(mid):
        answer = mid
        hi = mid-1
    else:
        lo = mid+1
print(answer)