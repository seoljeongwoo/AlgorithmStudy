import sys
sys.setrecursionlimit(10**9)

N,M = map(int,sys.stdin.readline().split())

answer = [[0] * (N + 1) for _ in range(N + 1)]

idx = [[] for _ in range(N + 1)]

maxInt = 987654321

for _ in range(M):
  Ai,Bi = map(int,sys.stdin.readline().split())
  idx[Ai].append(Bi)
  idx[Bi].append(Ai)

visited = []
distance = []

answerValue = []


def disValue(items):
  value = 0
  for item in range(1,len(items)):
    value = value + distance[item]
  return value


def dfs(i):
  visited[i] = True
  for start in idx[i]:
    if not visited[start]:
      if distance[start] == -1:
        distance[start] = distance[i] + 2
      else:
        if distance[start] > distance[i] + 2:
          distance[start] = distance[i] + 2
      dfs(start) 
  return

minValue = maxInt

for i in range(1,N + 1):
  for j in range(1,N + 1):
    if i == j:
      continue
    visited = [False] * (N + 1)
    distance = [-1] * (N + 1)
    distance[i] = 0
    dfs(i)
    visited = [False] * (N + 1)
    distance[j] = 0
    dfs(j)
    answer[i][j] = disValue(distance)
    if minValue > disValue(distance):
      minValue = disValue(distance)
      answerValue.append(i)
      answerValue.append(j)
      answerValue.append(minValue)

print('%d %d %d' %(answerValue[0],answerValue[1],answerValue[2]))

## 백준 결과는 부분성공
## 80ms 인데 정답이 안맞는 경우가 있는듯함.
## O(N^4)




