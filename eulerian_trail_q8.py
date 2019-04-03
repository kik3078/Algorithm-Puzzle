# Degree of All the vertices is even
# Only two vertices is odd
# width=10 height=10

def nCr(n, r):
    result = 1
    for i in range(1, n - r + 1):
        result *= (n - i + 1) / i
    return result

w, h = 10, 10
def answer(w, h):
    return 1 + 2 * nCr(9, 1)

print(answer(w, h))