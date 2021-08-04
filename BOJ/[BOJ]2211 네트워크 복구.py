import sys, heapq
input = sys.stdin.readline

n,m = map(int,input().rstrip('\n').split())
edge = [ [] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().rstrip('\n').split())
    edge[a].append((b,c))
    edge[b].append((a,c))

dist = [float('inf')] *(n+1)
parent = [-1]*(n+1)

dist[1] = 0
pq = []
heapq.heappush(pq,(dist[1],1))
while pq:
    dis, vertex = heapq.heappop(pq)
    if dist[vertex] > dis: continue
    
    for next_vertex, weight in edge[vertex]:
        if dist[next_vertex] <= dis + weight: continue
        dist[next_vertex] = dis + weight
        heapq.heappush(pq,(dis + weight, next_vertex))
        parent[next_vertex] = vertex

print(n-1)
for index in range(2,n+1):
    print(index, parent[index])