def find(r, c, sum_value):
    global min_value
    sum_value += arr[r][c]

    if r == n-1 and c == n-1:
        if min_value > sum_value:
            min_value = sum_value
        return

    if r < n-1:
        find(r+1, c, sum_value)
    if c < n-1:
        find(r, c+1, sum_value)


for tc in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    min_value = 100000
    find(0, 0, 0)
    print('#{} {}'.format(tc+1, min_value))