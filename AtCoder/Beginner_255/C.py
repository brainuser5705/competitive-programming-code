X, A, D, N = input().split(' ')
X, A, D, N = int(X), int(A), int(D), int(N)

# end value of the progression
end_range = (D*(N-1)+A)

# outside of progression (left side)
if (D < 0 and X > A) or (D > 0 and X < A):
    min_oper  = abs(X-A)

# outside of progression (right side)
elif (D < 0 and X < end_range) or (D > 0 and X > end_range):
    min_oper = abs(X - (D*(N-1)+A))

# self explanatory
# D == 0 if X is not equal to A
elif X == A or D == 0:
    min_oper = abs(X-A)

# between value of sequence
else:
    n = abs(X-A) // abs(D)
    first_n = D*(n)+A   # first value of between
    sec_n = D*(n+1)+A   # second value of between
    min_oper = min(abs(X-first_n), abs(X-sec_n))
 
print(min_oper)