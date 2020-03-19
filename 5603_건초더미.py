#건초더미 크기 모두 같게 만드는 데 필요한 최소 움직임의 횟수
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    l = []
    for _ in range(n):
        s = int(input())
        l.append(s)
    avg = sum(l) // n
    cnt = 0
    # while max(l) != min(l):
    for ele in l:
        if ele < avg:
            cnt += avg - ele

    print('#{} {}'.format(tc, cnt))