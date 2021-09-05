import sys
input = sys.stdin.readline
testcase = 1
while True:
    P,L,V = map(int,input().rstrip('\n').split())
    if not P and not L and not V: break
    print(f'Case {testcase}: {P*(V//L) + min((V%L),P)}')
    testcase +=1