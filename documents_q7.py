# A B C D E
# E move X 4 times move
# D - > 1
# E D    C - > 3
# C E D  B - > 4
# C B E D A -> 5

# A B C D E
# D E move X 3 times move
# D E     C - > 2
# D C E   B -> 4
# B D C E A -> 5

#def nCr(n, r):
#    result = 1
#    for i in range(1, n - r + 1):
#        result = result * (n - i + 1) / i
#    return result

N = 15

def nPr(n, r):
    result = 1
    for i in range(n, n - r, -1):
        result *= i
    return result

def check(N):
    cnt = 0
    for i in range(1, N):
        cnt += nPr(N, i - 1) * (N - i) * i
    return cnt

print(check(N))