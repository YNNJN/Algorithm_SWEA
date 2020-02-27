t = int(input())

for i in range(1, t+1):
    n = int(input())
    v = 0
    d = 0

    for j in range(n):
        info = input()
        if info[0] == '1':
            a = int(info[2])
            v += a

        if info[0] == '2':
            a = int(info[2])
            v -= a
            if v < 0:
                v = 0

        d += v
    print(f'#{i} {d}')