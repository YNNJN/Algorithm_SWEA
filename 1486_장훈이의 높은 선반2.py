total = 0
def dfs(a, k, n):
    global total
    if k == n:
        sum = 0
        for j in range(n):
            if a[j]:
                sum += data[j]
        if sum >= b:
            total = 0
            for j in range(n):
                if a[j]:
                    total += data[j]
            result.append(total)
    else:
        a[k] = 1
        dfs(a, k+1, n)
        a[k] = 0
        dfs(a, k+1, n)

for i in range(int(input())):
    n, b = map(int, input().split())
    data = list(map(int, input().split()))

    result = []
    a = [0] * b
    dfs(a, 0, n)
    print('#{} {}'.format(i + 1, min(result) - b))