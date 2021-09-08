import sys
input = sys.stdin.readline

def prime():
    isPrime = [False] * 1000001
    ret = {}
    for i in range(2,1001):
        if isPrime[i]: continue
        for j in range(i*i, 1000001, i):
            isPrime[j] = True
    for i in range(3, 1000001):
        if isPrime[i] == False:
            ret[i] = True
    return ret
oddPrime = prime()
while True:
    N = int(input())
    if N == 0 : break
    flag = False
    for k in oddPrime.keys():
        if (N-k) in oddPrime.keys():
            flag = True
            print(f'{N} = {k} + {N-k}')
            break
    if flag == False:
        print("Goldbach's conjecture is wrong.")
