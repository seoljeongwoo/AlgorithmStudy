import sys
sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline().rstrip())

V = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

## 1부터 스택 채우기 
answer = [1 for _ in range(N+1)]

def DFS(i):
  visited[i] = True
  
  for j in V[i]:
    start = j
    if not visited[start]:
      answer[start] = i
      DFS(start)
  return

for _ in range(N-1):
  x,y = map(int,sys.stdin.readline().split())
  V[x].append(y)
  V[y].append(x)


DFS(1)

for i in range(2,len(answer)):
  print(answer[i])
  

## 계속 런타임 에러가 나와서 검색해보니 재귀의 깊이를 늘려주면 된다고함.
## 재귀 사용 시 sys.setrecursionlimit(10 ** 6) 선택이 아닌 필수!
## 파이썬에 기본 재귀 깊이 제한이 1000으로 매우 얕은 편.
