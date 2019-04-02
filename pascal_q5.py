n = 45

def paskal(n):
    arr = [0] * (n + 1)
    arr[0] = 1
    for i in range(0, n):
        for j in range(i+1, 0, -1):
            arr[j] = arr[j-1] + arr[j]
    return arr

def check(n):
    arr = paskal(n)
    cnt = 2
    checker = [1, 5, 10, 50, 100, 500, 1000, 2000, 5000, 10000]
    for i in range(1, len(arr) - 1):
        for j in range(len(checker) - 1, -1, -1):
            result, arr[i] = divmod(arr[i], checker[j])
            cnt += result
    return cnt

print(check(n))