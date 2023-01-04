input()
A = input().split(" ")
Q = int(input())
for _ in range(Q):
    query = (input()).split(' ')
    if query[0] == '1':
        A[int(query[1])-1] = int(query[2])
    else:
        print(A[int(query[1])-1])