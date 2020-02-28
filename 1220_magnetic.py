for tc in range(1, 11):
    s = int(input())
    arr = [list(map(int, input().split())) for _ in range(s)]
    arr_copy = [[0 for _ in range(s)] for _ in range(s)]
    cnt = 0

    for i in range(s):
        for j in range(s):
            arr_copy[j][i] = arr[i][j]
    for i in range(s):
        l = []
        for j in range(s):
            if arr_copy[i][j] != 0:
                l.append(arr_copy[i][j])
            if len(set(l)) == 2:
                # if l[0] == 2 and l[-1] == 1:
                for k in range(len(l) + 1):
                    if k + 1 < len(l):
                        if l[k] == 1 and l[k + 1] == 2:
                            l = l[k + 1:]
                            cnt += 1
    print('#{} {}'.format(tc, cnt))