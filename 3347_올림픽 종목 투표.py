#가장 많은 표를 획득한 경기의 번호를 출력
for tc in range(int(input())):
    n,m = map(int, input().split())
    a = list(map(int, input().split())) #종목 목록
    b = list(map(int, input().split())) #위원 정보
    cnt = [0 for _ in range(n)]

    for i in range(m):
        for j in range(n):
            if b[i] >= a[j]:
                cnt[j] += 1
                break

    print('#{} {}'.format(tc + 1, cnt.index(max(cnt)) + 1))