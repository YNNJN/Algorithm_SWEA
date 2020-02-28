t = int(input())
for tc in range(1, t+1):
    n, b = map(int, input().split())
    s = list(map(int, input().split()))
    result = []
    min_value = 10000 * n
    for i in range(1 << n):
        value = 0
        for j in range(n):
            if i & (1 << j):
                value += s[j]
        if value >= b:
            if value < min_value:
                min_value = value
                result.append(min_value - b)
    print('#{} {}'.format(tc, result[-1]))