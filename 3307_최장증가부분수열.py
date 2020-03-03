#최대 증가 부분 수열의 길이
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    a = list(map(int, input().split()))
    d = [0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i] > a[j] and d[i] < d[j]:
                d[i] = d[j]
        d[i] += 1
    print('#{} {}'.format(tc, max(d)))
