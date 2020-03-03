t = int(input())
for tc in range(1, t+1):
    n,m = map(int, input().split()) #뿔, 짐승
    l = [0] * m
    for i in range(n):
        i = i % m
        l[i] += 1
    print('#{} {} {}'.format(tc, l.count(1), l.count(2)))

