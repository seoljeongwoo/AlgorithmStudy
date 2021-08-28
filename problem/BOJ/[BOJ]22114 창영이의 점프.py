import sys
input = sys.stdin.readline


N,K = map(int,input().rstrip('\n').split())
lst = list(map(int,input().rstrip('\n').split()))
A = [0]*(N+2)
for i in range(0,N-1):
    if lst[i] <= K:
        A[i+1] = A[i] + 1
    else:
        A[i+1] = 0
prev = 0
for i in range(N-1,0,-1):
    if prev == 0 and A[i] != 0:
        prev = A[i]
    if A[i] == 0:
        prev = 0
    else:
        A[i] = prev

ans = 0
for i in range(1,N):
    if A[i] == 0:
        ans = max(ans, A[i-1] + A[i+1] + 1)
    else:
        ans = max(ans, A[i])
print(ans+1)
