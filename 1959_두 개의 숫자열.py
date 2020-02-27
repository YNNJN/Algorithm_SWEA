t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    a_i= list(map(int, input().split(' ')))
    b_i= list(map(int, input().split(' ')))
    l = []

    (long_l, short_l) = (a_i,b_i) if len(a_i)>len(b_i) else (b_i,a_i)

    for k in range(len(long_l) - len(short_l)+1):
        total=0
        for j in range(len(short_l)):
            s = long_l[k+j] * short_l[j]
            total += s
        l.append(total)

    max_value = max(l)

    print(f'#{tc} {max_value}')



