t = int(input())
for tc in range(1, t+1):
    let = input().split()
    m = let[0]
    n = let[1]
    d = [[0]*(len(n)+1) for _ in range(len(m)+1)]

    for i in range(len(m)):
        for j in range(len(n)):
            if m[i] == n[j]:
                d[i + 1][j + 1] = d[i][j] + 1
            else:
                d[i + 1][j + 1] = max(d[i][j + 1], d[i + 1][j])
    print('#{} {}'.format(tc, d[len(m)][len(n)]))