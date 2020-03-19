#p/q 꼴로 출력
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    print('#{}'.format(tc), end=' ')
    for _ in range(n-1):
        print('1/{}'.format(n), end=' ')
    print('1/{}'.format(n))