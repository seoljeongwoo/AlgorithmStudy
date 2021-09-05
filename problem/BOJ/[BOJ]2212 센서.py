import sys
import heapq
input = sys.stdin.readline

N = int(input())
K = int(input())
pq = []
lst = list(map(int,input().rstrip('\n').split()))
lst = sorted(lst)
for index in range(1,N):
    heapq.heappush(pq, lst[index-1] - lst[index])

for i in range(min(len(pq),K-1)):
    heapq.heappop(pq)

print(abs(sum(pq)))