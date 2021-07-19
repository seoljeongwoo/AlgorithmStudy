import sys
input = sys.stdin.readline

inp = input().rstrip('\n')
rev_inp = ''.join(list(reversed(list(inp))))

print(1 if inp == rev_inp else 0)