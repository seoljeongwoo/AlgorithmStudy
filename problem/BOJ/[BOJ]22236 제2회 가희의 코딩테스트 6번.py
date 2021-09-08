import sys
input = sys.stdin.readline

d,m = map(int,input().rstrip('\n').split())
dp = [ [0 for col in range(d//2+5)] for row in range(d+5)]
dp[1][1] = 1
for row in range(1,d):
    for col in range(1,d//2+1):
        dp[row+1][col-1] = (dp[row+1][col-1] + dp[row][col])%m
        dp[row+1][col+1] = (dp[row+1][col+1] + dp[row][col])%m
print(dp[d][0])