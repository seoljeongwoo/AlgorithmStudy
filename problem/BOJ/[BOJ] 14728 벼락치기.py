import sys

scoreArr = [0]
timesArr = [0]

[N,Time] = list(map(int,sys.stdin.readline().rstrip().split()))

for _ in range(N):
  [K,S] = list(map(int,sys.stdin.readline().rstrip().split()))
  scoreArr.append(S)
  timesArr.append(K)

dp = [[0 for _ in range(Time + 1)] for _ in range(N + 1)] 
for i in range(1,N + 1):
  for j in range(1,Time + 1):
    if j >= timesArr[i]:
      dp[i][j] = max(dp[i-1][j],dp[i-1][j-timesArr[i]] + scoreArr[i])
    else:
      dp[i][j] = dp[i-1][j]

print(dp[N][Time])
    