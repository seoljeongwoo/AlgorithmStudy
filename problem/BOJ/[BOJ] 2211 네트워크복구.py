import sys

import heapq

input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]

inf = 987654321
dis = [inf] * (N+1)

times =[[0, 0]]+ [[inf, 0] for _ in range(N)]
times[1] = [0,0]
for _ in range(M):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))

def dijkstra(start):
  q = []
  heapq.heappush(q,(0,start))
  dis[start] = 0
  
  while q:
    value , now = heapq.heappop(q)

    if dis[now] < value:
      continue
    
    for item in graph[now]:
      cost = value + item[1]
      
      if cost < dis[item[0]]:
        dis[item[0]] = cost
        times[item[0]] = [now,item[0]]
        heapq.heappush(q,(cost,item[0]))

dijkstra(1)

answer= []

for i in range(2,N+1):
  answer.append((i,times[i][0]))

print(len(answer))
for a,b in answer:
  print('%d %d'%(a,b))


## 다익스트라 문제
## 답 구하는 곳에서 생각을 많이함.

## heapq 를 사용해서 O(nlogn)