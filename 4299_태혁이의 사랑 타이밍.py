#일, 시, 분
#11, 11, 11
t = int(input())
for tc in range(1, t+1):
    d,h,m = map(int, input().split())
    d = d-11
    h = h-11
    m = m-11
    time = m + 60*h + 24*60*d
    if time < 0:
        time = -1
    print('#{} {}'.format(tc, time))