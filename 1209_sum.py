for tc in range(1, 11):

    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_sum = 0

    for row in arr:
        if max_sum < sum(row):
            max_sum = sum(row)

    for col in range(100):
        col_sum = 0
        for row in arr:
            col_sum += row[col]
        if max_sum < col_sum:
            max_sum = col_sum

    for i in range(100):
        dia_sum = 0
        dia_sum += arr[i][i]
    if max_sum < dia_sum:
        max_sum = dia_sum

    print(f'#{tc} {max_sum}')