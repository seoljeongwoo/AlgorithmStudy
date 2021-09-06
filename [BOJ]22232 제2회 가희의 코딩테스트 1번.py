import sys
input = sys.stdin.readline

N,M = map(int,input().rstrip('\n').split())
files = [ input().rstrip('\n') for _ in range(N)]
extensions = { input().rstrip('\n') : True for _ in range(M) }
sort = []
for file in files:
    file_name, extension_name = file.split('.')
    sort.append((file_name, 1 if extension_name in extensions.keys() else 2, extension_name, file_name + '.' + extension_name))
sort = sorted(sort)
for data in sort:
    print(data[3])