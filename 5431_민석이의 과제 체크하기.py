t = int(input())
for tc in range(1, t+1):
    n,k = map(int, input().split())
    number = list(map(int, input().split()))
    total = list(range(1, n + 1))
    for num in number:
        if num in total:
            total.remove(num)
    print('#{} {}'.format(tc, ' '.join(map(str,total))))

