for tc in range(int(input())):
    n,m = map(int, input().split())
    c = list(map(int, input().split()))
    arr = [[c[i], i+1] for i in range(n)]
    i = n
    while len(arr) > 1:
        if arr[0][0] != 0:
            arr[0][0] //= 2
            if arr[0][0] == 0:
                arr.pop(0)
                if i < m:
                    arr.append([c[i], i+1])
                    i += 1
            else:
                x = arr.pop(0)
                arr.append(x)

    print('#{} {}'.format(tc+1, arr[0][1]))