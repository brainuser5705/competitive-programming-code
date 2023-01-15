# N, M = map(int, input().split())
# visited = set()

# count = 0
# for _ in range(M):
#     u1, u2 = map(int, input().split())
#     if u1 not in visited and u2 not in visited:
#         count += 1
#     visited.add(u1)
#     visited.add(u2)
    
# print(count + N - len(visited)) # count + any single vertices

# N, M = map(int, input().split())
# arr = [[0 for _ in range(1)] for _ in range(N)]

# for _ in range(M):
#     u1, u2 = map(int, input().split())
#     arr[u1-1] += [u2]
#     arr[u2-1] += [u1]

# visited = set()
# count = 0
# for i in range(N):

#     count += 1
#     visited.add(i+1)
#     connected = False

#     for j in range(1, len(arr[i])):
#         itm = arr[i][j]
#         if itm in visited:
#             connected = True
#             continue
#         visited.add(itm)

#     if connected:
#         count -= 1

# print(count)


# doesn't work for 1 - 4 - 3 - 2 connection


N, M = map(int, input().split())
arr = [[0 for _ in range(1)] for _ in range(N)]

for _ in range(M):
    u1, u2 = map(int, input().split())
    arr[u1-1] += [u2]
    arr[u2-1] += [u1]


visited = set()

def visit(n):
    count = 0
    if n not in visited:
        count = 1
        visited.add(n)
        for j in range(1, len(arr[n-1])):
            itm = arr[n-1][j]
            visit(itm) # to avoid needing double directions - if count is 0, then it is connected
    return count

n = 1
connections = 0
while len(visited) != N:
    connections += visit(n)
    n += 1

print(connections)