for tc in range(int(input())):
    n = float(input())
    ans = ''
    for i in range(1, 13):
        if n == 0:
            break
        div = 2**(-i)
        if n >= div:
            n -= div
            ans += '1'
        else:
            ans += '0'
    if n:
        ans = 'overflow'

    print('#{} {}'.format(tc+1, ans))