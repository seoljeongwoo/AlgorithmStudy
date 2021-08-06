import sys

N,K = map(int,sys.stdin.readline().rstrip('\n').split())

dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]

T = [0 for _ in range(K + 1)]
S = [0 for _ in range(K + 1)]

for i in range(1,K + 1):
  s,t = map(int,sys.stdin.readline().rstrip('\n').split())
  S[i] = s
  T[i] = t

for i in range(1, K + 1):
  for j in range(1, N + 1):
    if j < T[i]:
      dp[i][j] = dp[i-1][j]
    
    if j >=T[i]:
      dp[i][j] = max(dp[i-1][j] , S[i] + dp[i - 1][j - T[i]])


print(dp[K][N])

## 기본 dp (배낭 문제)

## 0,1 배낭 문제는 dp로 풀고

## 쪼갤수 있는 배낭 문제는 그리디 알고리즘으로 풀기
