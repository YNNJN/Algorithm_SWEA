t = int(input())

for tc in range(1, t+1):
    n = int(input())
    s = 0

    for i in range(1, n+1):
        if i % 2:
            s += i

        else:
            s -= i

    print(f'#{tc} {s}')