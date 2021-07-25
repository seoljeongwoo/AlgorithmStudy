import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    original_A,original_B = input().rstrip('\n').split()
    A,B = list(original_A) , list(original_B)
    A.sort()
    B.sort()

    isAnagram = False
    if len(A) == len(B):
        for i in range(len(A)):
            if A[i] != B[i]:
                break
            if i == len(A) -1:
                isAnagram = True

    print(f'{original_A} & {original_B} are anagrams.' if isAnagram == True else f'{original_A} & {original_B} are NOT anagrams.')
