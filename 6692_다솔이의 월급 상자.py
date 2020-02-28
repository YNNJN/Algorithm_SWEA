t = int(input())
for tc in range(1, t+1):
    treat = 0
    n = int(input())

    for _ in range(n):
        p, x = map(float, input().split())
        treat += p * x

    print('#{}'.format(tc), end = ' ')
    print('%0.6f' % treat)

