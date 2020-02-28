def search(r,c,board):
    dr = [0, 0, -1]
    dc = [-1, 1, 0]
    visited = []

    while r > 0:
        for i in range(3):
            tr = r + dr[i]
            tc = c + dc[i]

            if tr < 0 or tc < 0 or tr > 99 or tc > 99:
                continue
            if board[tr][tc] == 0:
                continue
            if (tr, tc) in visited:
                continue

            else:
                visited.append((tr,tc))
                r = tr
                c = tc
                break
    return c

for tc in range(1, 11):
    t = input()
    board = [list(map(int, input().split())) for _ in range(100)]

    x = 99
    y = 0
    for j in range(100):
        if board[99][j] == 2:
            y = j
    print('#{} {}'.format(tc, search(x,y,board)))