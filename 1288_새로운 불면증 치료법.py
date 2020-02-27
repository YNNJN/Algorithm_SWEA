t = int(input())
for i in range(1, t + 1):
    result = set()
    n = int(input())
    k = 1

    while result != {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
        m = k * n
        m = str(m)
        for j in range(len(m)):
            result.add(m[j])
        k += 1
    print(f'#{i} {m}')