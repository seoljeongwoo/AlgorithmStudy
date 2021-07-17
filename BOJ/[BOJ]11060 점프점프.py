import sys
input = sys.stdin.readline

N = int(input())
maze = list(map(int,input().rstrip('\n').split()))
INF = int(1e9)
DP = [INF]*(N)
DP[0] = 0

for currentPosition in range(0,N,1):
    for jump in range(1,maze[currentPosition]+1,1):
        nextPosition = currentPosition + jump
        if nextPosition >= N :
            break
        DP[nextPosition] = min(DP[nextPosition] , DP[currentPosition] + 1)
print(DP[N-1] if DP[N-1] != INF else -1)

'''
다이나믹 프로그래밍을 이용하여 문제를 해결함.
DP[i] = i칸에 위치할때 최소 점프횟수로 정의하여 문제를 해결함.
아아아
'''