def search(r,c,board):
    global flag
    if flag:
        return

    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]

    board[r][c] = 1
    for i in range(4):
        tr = r + dr[i]
        tc = c + dc[i]

        if not (0 <= tr < 16 and 0 <= tc < 16):
            continue

        if board[tr][tc] == 3:
            flag = True
            return
        elif board[tr][tc] == 1:
            continue
        search(tr, tc, board)

for tc in range(1, 11):
    t = input()
    board = [list(map(int, input())) for _ in range(16)]
    flag = False
    search(1,1,board)

    print('#{}'.format(tc), end=' ')
    if flag:
        print(1)
    else:
        print(0)