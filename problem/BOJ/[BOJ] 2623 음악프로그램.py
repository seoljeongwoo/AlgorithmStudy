import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())

graph = [[] for _ in range( N + 1 )]
degree = [0] * (N + 1)
answer = []
queue = deque()
empty = 0

for _ in range(M):
  arr = list(map(int,sys.stdin.readline().split()))
  for i in range(1,arr[0]):
    graph[arr[i]].append(arr[i + 1])
    degree[arr[i+1]] += 1

for i in range(1, N + 1):
  if degree[i] == 0:
    queue.append(i)

while len(queue) != 0:
  start = queue.popleft()
  answer.append(start)
  for v in graph[start]:
    degree[v] -=1
    if degree[v] == 0:
      queue.append(v)

if len(answer) != N:
  print(0)
else:
  for item in answer:
    print(item)


## keyword : 위상정렬

## 하나의 방향 그래프에서 진입 간선에 갯수가 0인 노드 부터 큐에 넣음.
## 차례대로 큐를 제거하면서 연결 간선을 큐에 넣음.
## 진입 간선 갯수가 0인 노드가 없으면 위상 정렬 알고리즘 불가

## 위상정렬을 공부 후 문제 품.
