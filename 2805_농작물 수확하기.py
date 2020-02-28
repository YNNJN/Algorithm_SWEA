t = int(input())
for tc in range(1, t+1):
    n = int(input())
    value = [list(map(int, input())) for _ in range(n)]
    profit = []

    for i in range(n//2+1):
        mid = value[i][n//2-i:n//2+i+1]
        profit.append(sum(mid))

    for m in range(n-1, n//2, -1):
        mid = value[m][n//2-(n-1-m):n//2+(n-1-m)+1]
        profit.append(sum(mid))

    s = sum(profit)
    print('#{0} {1}'.format(tc, s))
