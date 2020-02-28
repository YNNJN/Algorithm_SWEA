t = int(input())
for tc in range(1, t+1):
    scr = list(map(int, input().split()))
    for i in range(len(scr)):
        if scr[i] <= 40:
            scr[i] = 40
    avg = sum(scr)//len(scr)
    print('#{} {}'.format(tc, avg))