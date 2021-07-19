import sys
input = sys.stdin.readline

N,T = map(int,input().rstrip('\n').split())
DP = [0]*(T+1)

for query in range(N):
    K,S = map(int,input().rstrip('\n').split())
    for usedTime in range(T,K-1,-1):
        DP[usedTime] = max(DP[usedTime] , DP[usedTime - K] + S)

print(DP[T])

'''

Key Idea = Dynamic Programming (Kanpsack Problem)
DP[i] = i시간 공부했을때 가질수있는 최대점수
usedTime 을 T초부터 K-1초로 돌린이유는 같은공부를 여러번적용될수있기 때문.

'''
