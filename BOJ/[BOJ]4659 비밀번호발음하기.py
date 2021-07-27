import sys
input = sys.stdin.readline
target = 'aeoiu'

while True:
    inp = input().rstrip('\n')
    if inp == 'end' :
        break

    lst = list(inp)
    three, two, one = False, False, False
    for index, data in enumerate(lst):
        if data in target: one = True
        if index > 0 and data == lst[index-1] and data != 'e' and data !='o': two = True
        if index > 1 and (data in target) and (lst[index-1] in target) and (lst[index-2] in target) : three = True
        if index > 1 and (data not in target) and (lst[index-1] not in target) and (lst[index-2] not in target) : three = True
    print(f'<{inp}> is acceptable.' if one == True and two == False and three == False else f'<{inp}> is not acceptable.')
    
    