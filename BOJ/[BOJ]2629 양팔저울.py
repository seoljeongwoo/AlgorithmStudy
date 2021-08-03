import sys
input = sys.stdin.readline

wc = int(input())
wl = list(map(int,input().rstrip('\n').split()))
cc = int(input())
cl = list(map(int,input().rstrip('\n').split()))
offset = 40005
dp = [[False]*2*offset for _ in range(wc+1)]
dp[0][0+offset] = True
for row in range(0,wc):
    for col in range(0,2*offset):
        if dp[row][col] == True:
            dp[row+1][col] = True
            dp[row+1][col+wl[row]] = True
            dp[row+1][col-wl[row]] = True
for data in cl:
    print('Y' if dp[wc][data+offset] == True else 'N' , end = ' ')
