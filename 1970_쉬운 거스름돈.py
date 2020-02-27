t = int(input())

for tc in range(1, t+1):
    n = int(input())
    n = n - (n % 10)
    cnt_list = [0 for _ in range(8)]

    while n != 0:
        while n >= 50000:
            n -= 50000
            cnt_list[0] += 1

        while n >= 10000:
            n -= 10000
            cnt_list[1] += 1

        while n >= 5000:
            n -= 5000
            cnt_list[2] += 1

        while n >= 1000:
            n -= 1000
            cnt_list[3] += 1

        while n >= 500:
            n -= 500
            cnt_list[4] += 1

        while n >= 100:
            n -= 100
            cnt_list[5] += 1

        while n >= 50:
            n -= 50
            cnt_list[6] += 1

        while n >= 10:
            n -= 10
            cnt_list[7] += 1

    print(f'#{tc}')
    [print(ele, end = ' ') for ele in cnt_list]
    print()