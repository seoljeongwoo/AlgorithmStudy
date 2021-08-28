import sys
input = sys.stdin.readline

N,K = map(int,input().rstrip('\n').split())
lst = list(map(int,input().rstrip('\n').split()))

DP = [float('inf')] * (K+1)
DP[0] = 0
for c in lst:
    for i in range(K,c-1,-1):
        DP[i] = min(DP[i] , DP[i-c] + 1)
print( DP[K] if DP[K] != float('inf') else -1)