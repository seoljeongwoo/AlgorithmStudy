import sys
input = sys.stdin.readline
l = int(input())
lst = list(map(int,input().rstrip('\n').split()))
n = int(input())
l,r = 1, 1000
for data in lst:
    if data <= n:
        l = max(l, data+1)
    if data >=n:
        r = min(r, data-1)
ret = 0
for i in range(l,r+1):
    for j in range(i+1,r+1):
        if i<= n <=j: 
            ret+=1
print(ret)

## 기존 코드

# import sys

# input = sys.stdin.readline

# N = int(input())
# S = list(map(int,input().rstrip('\n').split()))
# n = int(input())

# fr = 0
# se = 0

# S.sort()

# for i in range(N):
#   if S[i] >= n:
#     if i != 0:
#       fr = n - S[i - 1]
#       se = S[i] - n
#     break

# if fr * se == 0:
#   print(0)
# else:
#   print((fr * se) - 1)


## 기존 나의 코드는 n 을 기준으로 양 옆 숫자와 비교 후 갯수를 곱하여 중복인 1 을 빼주는 코드

## 위의 수정 코드는 구간을 직접 구해 이중포문으로 해결

