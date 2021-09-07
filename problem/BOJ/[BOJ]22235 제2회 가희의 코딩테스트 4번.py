import sys , heapq
from collections import defaultdict
input = sys.stdin.readline
N,M = map(int,input().rstrip('\n').split())
#1 2 3 4 dimension
ballon_diagonal = [ defaultdict(list) for _ in range(4)]
ballon_diagonal_sum = [ defaultdict(int) for _ in range(4)]
#up down right left
ballon_straight = [ list() for _ in range(4)]
ballon_straight_sum = [0]*4

def gcd(a,b):
    return a if b == 0 else gcd(b, a%b)

for _ in range(N):
    x, y, life = map(int,input().rstrip('\n').split())

    if x == 0:
        if y > 0 : heapq.heappush(ballon_straight[0],life)
        else : heapq.heappush(ballon_straight[1], life)
        continue
    elif y == 0:
        if x > 0 : heapq.heappush(ballon_straight[2], life)
        else : heapq.heappush(ballon_straight[3], life)
        continue
    index = -1
    if x > 0 and y > 0: index = 0
    elif x > 0 and y < 0: index = 3
    elif x < 0 and y > 0: index = 1
    else : index = 2
    x = abs(x)
    y = abs(y)
    _gcd = gcd(x,y)
    key = (x//_gcd, y//_gcd)
    heapq.heappush(ballon_diagonal[index][key], life)

ret = N

for _ in range(M):
    x, y, attack = map(int,input().rstrip('\n').split())
    if x == 0:
        if y > 0 :
            ballon_straight_sum[0] += attack
            while ballon_straight[0] and ballon_straight[0][0] <= ballon_straight_sum[0]:
                ret -=1
                heapq.heappop(ballon_straight[0])
        else : 
            ballon_straight_sum[1] += attack
            while ballon_straight[1] and ballon_straight[1][0] <= ballon_straight_sum[1]:
                ret -=1
                heapq.heappop(ballon_straight[1])
        print(ret)
        continue
    elif y == 0:
        if x > 0 : 
            ballon_straight_sum[2] += attack
            while ballon_straight[2] and ballon_straight[2][0] <= ballon_straight_sum[2]:
                ret -= 1
                heapq.heappop(ballon_straight[2])
        else :
            ballon_straight_sum[3] += attack
            while ballon_straight[3] and ballon_straight[3][0] <= ballon_straight_sum[3]:
                ret -= 1
                heapq.heappop(ballon_straight[3])
        print(ret)
        continue

    index = -1
    if x > 0 and y > 0: index = 0
    elif x > 0 and y < 0: index = 3
    elif x < 0 and y > 0: index = 1
    else : index = 2
    x = abs(x)
    y = abs(y)
    _gcd = gcd(x,y)
    key = (x//_gcd, y//_gcd)
    ballon_diagonal_sum[index][key] += attack
    if key in ballon_diagonal[index].keys():
        while ballon_diagonal[index][key] and ballon_diagonal[index][key][0] <= ballon_diagonal_sum[index][key]:
            ret -= 1
            heapq.heappop(ballon_diagonal[index][key])
    print(ret)
