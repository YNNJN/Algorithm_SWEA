t = int(input())
for tc in range(1, t+1):
    d,a,b,f = map(int, input().split())
    num = f*d/(a+b)
    print('#{}'.format(tc), end=' ')
    print('%.10f' % num)