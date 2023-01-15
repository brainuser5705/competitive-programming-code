T = int(input())
for _ in range(T):
    N = int(input())
    A = input().split(' ')
    count = 0
    for i in range(N):
        if int(A[i]) % 2 == 1:
            count += 1
    print(count)