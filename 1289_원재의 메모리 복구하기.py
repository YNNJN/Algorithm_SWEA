#원래 값으로 복구하기 위한 최소 수정 횟수
t = int(input())
for tc in range(t):
    a = list(map(int,input()))
    cur = a[0]
    if a[0] == 1:
        cnt = 1
    else:
        cnt = 0
    for i in range(1,len(a)):
        if a[i] == cur:
            continue
        else:
            cnt += 1
            cur = a[i]
    print('#{} {}'.format(tc+1, cnt))