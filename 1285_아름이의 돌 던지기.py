t = int(input())
for i in range(1, t + 1):
    mem = int(input())
    d = input().replace('-', '')
    d_list = d.split(' ')
    print(type(map(int, d_list)))
    d_list = list(map(int, d_list))

    m = min(d_list)
    count = 0
    for num in d_list:
        if num == m: count += 1

    print(f'#{i} {m} {count}')