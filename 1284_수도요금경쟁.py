t = int(input())
for i in range(1, t+1):
    p, q, r, s, w = map(int, input().split(' '))
    price_a = w * p

    if w < r:
        price_b = q
        if price_a > price_b:
            print(f'#{i} {price_b}')
        else:
            print(f'#{i} {price_a}')
    else:
        price_b = q + s * (w - r)
        if price_a > price_b:
            print(f'#{i} {price_b}')
        else:
            print(f'#{i} {price_a}')
